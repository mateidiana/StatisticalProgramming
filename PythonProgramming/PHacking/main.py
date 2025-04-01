# Illustration of the danger associated with p-hacking. Generate n random coin flips
# with a fair coin, and compute the p-value for the hypothesis that the coin is fair or not
# Start with n = 20 and then increase the number of coin flips to n = 50, computing the p-value
# each time, and then plot the p-value versus n. The goal is to show that sometimes retesting
# will cause the p-value to indicate a significant result even if it isn't true

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binomtest

np.random.seed(41)


# Function to simulate coin flips and compute the p-value
def compute_p_value(flips):
    heads = np.sum(flips)  # Count the number of heads
    n_flips = len(flips)

    # Compute the p-value for the hypothesis that the coin is fair (two-tailed test)
    p_value = binomtest(heads, n=n_flips, p=0.5, alternative='two-sided').pvalue

    return p_value


# Start with n=20 coin flips
initial_n = 20
additional_n = 30
total_n = initial_n + additional_n

# Simulate the initial 20 coin flips
flips = np.random.binomial(n=1, p=0.5, size=initial_n)

# Initialise lists to store the number of flips and corresponding p-values
n_values = list(range(initial_n, total_n+1))
p_values = []

# Compute the p-value for each step as additional coin flips are added
for i in range(additional_n + 1):
    # Compute the p-value with the current number of flips
    p_value = compute_p_value(flips)
    p_values.append(p_value)

    # Add one more coin flip (unless we've reached the maximum)
    if len(flips) < total_n:
        new_flip = np.random.binomial(n=1, p=0.5)
        flips = np.append(flips, new_flip)


# Plot p-value vs number of coin flips
plt.figure(figsize=(10, 6))
plt.plot(n_values, p_values, marker='o', linestyle='-', color='blue')
plt.axhline(y=0.05, color='red', linestyle='--', label='Significance level (p=0.05)')
plt.title('P-value vs Number Of Coin Flips')
plt.xlabel('Number of Coin Flips (n)')
plt.ylabel('P-value')
plt.legend()
plt.grid(True)
plt.show()

