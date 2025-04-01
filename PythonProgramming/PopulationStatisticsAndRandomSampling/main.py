import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from scipy.stats import norm

# Set the random seed for reproducibility (optional)
# np.random.seed(42)

# Step 1: Generate N=1000 random samples from a Poisson distribution with a mean of lambda
lambda_value = 10
N = 10000
DataPopulation = np.random.poisson(lam=lambda_value, size=N)


# Step 2: Draw a random subset of n = 30 samples from DataPopulation
n = 200
DataSample = np.random.choice(DataPopulation, size=n, replace=False)

# Step 3: Compute the mean and standard deviation of both vectors
mean_population = np.mean(DataPopulation)
std_population = np.std(DataPopulation)

mean_sample = np.mean(DataSample)
std_sample = np.std(DataSample)

# Print the results
print("Population mean:", mean_population)
print("Population Standard Deviation:", std_population)
print("Sample Mean:", mean_sample)
print("Sample Standard Deviation", std_sample)


# Generate a histogram of DataPopulation
plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(DataPopulation, bins=19, color='blue', edgecolor='black', alpha=0.6, density=True)

# Plot the Poisson distribution that best fits the population mean
x = np.arange(0, bins[-1] + 1)
pmf_values = poisson.pmf(x, mu=mean_population)
plt.plot(x, pmf_values, 'k-', marker='o', label=f'Poisson pmf (mean = {mean_population:.2f})')

# Label the axes
plt.xlabel('Value')
plt.ylabel('Probability density')
plt.title('Histogram of DataPopulation with Fitted Poisson Distribution')

plt.legend()
plt.show()




n = 30  # sample size
m = 100  # number of samples to take

# Initialise arrays to store sample means and std deviations
SampleMeans = np.zeros(m)
SampleSTDs = np.zeros(m)

# Repeat sampling m times
for i in range(m):
    DataSample = np.random.choice(DataPopulation, size=n, replace=False)
    SampleMeans[i] = np.mean(DataSample)
    SampleSTDs[i] = np.std(DataSample)


# Plot a histogram of the SampleMeans
plt.figure(figsize=(10, 6))
plt.hist(SampleMeans, bins=15, color='red', edgecolor='black', alpha=0.7)
plt.title('Histogram of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()




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

