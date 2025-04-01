# Alpha particles emitted by Americium 241
# Example from Rice, taken from Berkson 1966
# 10220 Gieger clicks (emissions) were measured, specifically time between clicks
# Data is binned into 10-second intervals
# Clicks per 10-second interval should be Poisson (time between is exponential)

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Data
ClicksPerTenSeconds = np.arange(18)  # Number of counts per 10-second interval
ObservedCounts = [1, 6, 11, 28, 56, 105, 126, 146, 164, 161, 123, 101, 74, 53, 23, 15, 9, 5]

# Plotting the observed data
plt.figure(figsize=(10, 6))
plt.plot(ClicksPerTenSeconds, ObservedCounts, marker='o', linestyle='-', color='blue', label='Observed data')

# Calculate the sample mean
sample_mean = np.average(ClicksPerTenSeconds, weights=ObservedCounts)

# Fit a poisson distribution using the sample mean as lambda
poisson_dist = poisson.pmf(ClicksPerTenSeconds, mu=sample_mean) * np.sum(ObservedCounts)

# Plotting the poisson distribution
plt.plot(ClicksPerTenSeconds, poisson_dist, marker='x', linestyle='--', color='red', label='Poisson distribution with '
                                                                                           f'lambda={sample_mean:.2f}')

# Adding labels and title
plt.title('Observed Alpha Particle Emissions per 10-second interval', fontsize=14)
plt.xlabel('Number of Clicks per 10-second interval', fontsize=12)
plt.ylabel('Observed count', fontsize=12)
plt.grid(True)
plt.legend()

# Set x-axis to display integer tick marks only
plt.xticks(ticks=np.arange(0, max(ClicksPerTenSeconds)+1, 1))
plt.show()

