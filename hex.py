#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from math import sqrt

# Generate some random data

ss = 0.
x = [1.5-ss, 4.5-ss, 7.5-ss, 3-ss, 6-ss, 1.5-ss, 4.5-ss, 7.5-ss]

s3 = sqrt(3)

y = [1*s3-ss, 1*s3-ss, 1*s3-ss, 2.5*s3-ss, 2.5*s3-ss, 4*s3-ss, 4*s3-ss, 4*s3-ss]

# Create a hexagonal 2D histogram
fig, ax = plt.subplots()  
hexbin = ax.hexbin(x, y, gridsize=(3,2), cmap='Blues', extent=(0, 5*sqrt(3), 0, 9))   # , gridsize=(3,2) -7.5, 6, -5.598076211353316, 5.598076211353316  extent=(0, 5*sqrt(3), 0, 9)

# Add a colorbar
cbar = plt.colorbar(hexbin)
cbar.set_label('Counts')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Hexagonal 2D Histogram')

# Show the plot
plt.show()