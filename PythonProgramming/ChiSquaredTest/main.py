# Given data and a fit in form of a probability distribution f, is the fit good?

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, chi2

# Data
n = np.arange(18)  # Number of counts per 10-second interval
Observed = [1, 6, 11, 28, 56, 105, 126, 146, 164, 161, 123, 101, 74, 53, 23, 15, 9, 5]

# Combine the first three bins into one bin
Observed_combined = np.copy(Observed)
Observed_combined[2] = np.sum(Observed[0:3])
Observed_combined = np.delete(Observed_combined, [0, 1])

# Adjust n to match the combined bin
n_combined = np.copy(n)
n_combined[2] = 2
n_combined = np.delete(n_combined, [0, 1])

# Calculate the sample mean (lambda estimate)
sample_mean = np.average(n, weights=Observed)

# Total number of observations
total_counts = np.sum(Observed)

# Compute expected frequencies for each bin using Poisson distribution
poisson_probs = poisson.pmf(n, mu=sample_mean)
Expected = poisson_probs * total_counts

# Combine the first three bins of expected frequencies
Expected_combined = np.copy(Expected)
Expected_combined[2] = np.sum(Expected[0:3])
Expected_combined = np.delete(Expected_combined, [0, 1])

# Perform the chi-squared test
chi_squared_stat = np.sum((Observed_combined - Expected_combined) ** 2 / Expected_combined)

degrees_of_freedom = len(Observed_combined) - 1 - 1

p_value = 1 - chi2.cdf(chi_squared_stat, df=degrees_of_freedom)

print(f'Chi-squared statistic: {chi_squared_stat:.4f}')
print(f'Degrees of freedom: {degrees_of_freedom}')
print(f'P-value: {p_value:.4f}')

# Plot the chi-squared pdf
x = np.linspace(0, 40, 1000)
pdf = chi2.pdf(x, df=degrees_of_freedom)

# Rejection region for 95% confidence interval (alpha = 0.05)
critical_value = chi2.ppf(0.95, df=degrees_of_freedom)

plt.figure(figsize=(10, 6))

# Plot the pdf of chi-square
plt.plot(x, pdf, 'b-', lw=2, label=f'Chi-squared PDF (df={degrees_of_freedom}')
plt.fill_between(x, pdf, where=(x >= critical_value), color='red', alpha=0.3, label='Rejection region')
plt.axvline(x=chi_squared_stat, color='green', linestyle='--',label=f'Chi-squared stat = {chi_squared_stat:.2f}')
plt.axvline(x=critical_value, color='red', linestyle='--', label=f'Critical value = {critical_value:.2f}')

plt.title('Chi-squared test probability density function', fontsize=14)
plt.xlabel('Chi-squared value', fontsize=12)
plt.ylabel('Pdf', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

if chi_squared_stat > critical_value:
    print('Reject the null hypothesis: The data is not consistent with a Poisson distribution')
else:
    print('Failed to reject the null hypothesis: The data is consistent with a Poisson distribution')