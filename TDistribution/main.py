# Useful especially for hypothesis testing with small sample size n

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm
from matplotlib import cm

# Range of x values for plotting
x = np.linspace(-5, 5, 1000)

# Degrees of freedom to demonstrate convergence
degrees_of_freedom = [1, 2, 5, 10, 30, 100]

# Use the inverted viridis colormap
cmap = plt.get_cmap('viridis_r', len(degrees_of_freedom))

plt.figure(figsize=(10, 6), facecolor='white')
ax = plt.gca()
ax.set_facecolor('white')

# Plot the normal distribution (standard normal, mean=0, std=1)
plt.plot(x, norm.pdf(x), 'k--', lw=2, label='Standard Normal Distribution')

# Plot the t-distribution for different degrees of freedom
for i, df in enumerate(degrees_of_freedom):
    plt.plot(x, t.pdf(x, df), lw=2, color=cmap(i), label=f't-distribution (df={df})')

plt.title('Convergence of t-distribution to normal distribution', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('PDF', fontsize=12)
plt.legend(facecolor='white', framealpha=1, edgecolor='black', labelcolor='black')
ax.tick_params(colors='black')
plt.grid(True, color='gray', alpha=0.5)
plt.show()