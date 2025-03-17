# Bootstrap estimate error in lambda

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

# Data
n = np.arange(18)  # Number of counts per 10-second interval
Observed = [1, 6, 11, 28, 56, 105, 126, 146, 164, 161, 123, 101, 74, 53, 23, 15, 9, 5]

# Calculate the sample mean (initial estimate of lambda)
sample_mean = np.average(n, weights=Observed)

# Number of bootstrap samples
num_bootstrap = 1000
bootstrap_lambdas = []

# Bootstrap procedure
for _ in range(num_bootstrap):
    # Generate a synthetic dataset using the estimated lambda
    synthetic_data = np.random.poisson(lam=sample_mean, size=np.sum(Observed))

    # Bin the synthetic data to match the observed format (nr of counts per 10 sec interval)
    synthetic_hist, _ = np.histogram(synthetic_data, bins=np.arange(19))

    # Calculate the new lambda estimate from the synthetic data
    new_lambda = np.average(n, weights=synthetic_hist)

    # Store the new lambda estimate
    bootstrap_lambdas.append(new_lambda)

# Calculate the sample standard deviation of the observed data
observed_std = np.sqrt(np.average((n - sample_mean) ** 2, weights=Observed))

# Calculate the clt-based standard deviation for lambda estimates
clt_std = observed_std / np.sqrt(sum(Observed))

# Plot the distribution of bootstrap lambda estimates
plt.figure(figsize=(10, 6))
plt.hist(bootstrap_lambdas, bins=30, color='green', edgecolor='black', alpha=0.7, density=True)

# Generate the normal distribution using the clt approximation
x = np.linspace(min(bootstrap_lambdas), max(bootstrap_lambdas), 1000)
normal_approximation = norm.pdf(x, loc=sample_mean, scale=clt_std)

# Plot the normal distribution on top of the histogram
plt.plot(x, normal_approximation, 'r-', lw=2, label=f'Normal approximation (mean={sample_mean:.2f})')

plt.title('Bootstrap distribution of lambda estimates with Normal approximation', fontsize=12)
plt.xlabel('Lambda estimate', fontsize=11)
plt.ylabel('Density', fontsize=11)
plt.legend()
plt.grid(True)
plt.show()
