#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from math import sqrt

# Generate some random data

ss = 0.
x = [0, 1.5-ss, 4.5-ss, 7.5-ss, 3-ss, 6-ss, 1.5-ss, 4.5-ss, 7.5-ss]

s3 = sqrt(3)

y = [0, 1*s3-ss, 1*s3-ss, 1*s3-ss, 2.5*s3-ss, 2.5*s3-ss, 4*s3-ss, 4*s3-ss, 4*s3-ss]

# Create a hexagonal 2D histogram
fig, ax = plt.subplots()  
plt.scatter(x, y,cmap = 'hot_r', s = 10000, marker=u'$\u2B23$')

# Add a colorbar
#cbar = plt.colorbar()
#cbar.set_label('Counts')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Hexagonal 2D Histogram')

# Show the plot
plt.show()