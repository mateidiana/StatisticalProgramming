import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm

# Generate N=1000 random samples from a Poisson distribution with a mean of lambda
lambda_value = 10
N = 10000
DataPopulation = np.random.poisson(lam=lambda_value, size=N)

n = 100  # sample size
m = 1000  # number of samples to take

# Initialise arrays to store sample means and std deviations
SampleMeans = np.zeros(m)
SampleSTDs = np.zeros(m)

# Repeat sampling m times
for i in range(m):
    DataSample = np.random.choice(DataPopulation, size=n, replace=False)
    SampleMeans[i] = np.mean(DataSample)
    SampleSTDs[i] = np.std(DataSample)


# Calculate the population mean and std deviation
mean_population = np.mean(DataPopulation)
std_population = np.std(DataPopulation)

# Compute the standard deviation of the sample means
std_error = std_population / np.sqrt(n)

# Generate the normal distribution that approximates the distribution of sample means
x = np.linspace(min(SampleMeans), max(SampleMeans), 100)
normal_approximation = norm.pdf(x, loc=mean_population, scale=std_error)

# Plot the histogram of SampleMeans
plt.figure(figsize=(10, 6))
plt.hist(SampleMeans, bins=15, color='red', edgecolor='black', alpha=0.7, density=True)

# Plot the normal distribution approximation on top of the histogram
plt.plot(x, normal_approximation, 'b-', label=f'Normal Approximation\n(mean={mean_population:.2f})')
plt.xlabel('Sample mean')
plt.ylabel('Density')
plt.title('Histogram of Sample Means with Normal Approximation')
plt.legend()
plt.show()

