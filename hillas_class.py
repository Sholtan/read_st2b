#!/usr/bin/env python3
from math import asin
from math import sin
from math import pi
from math import sqrt
from math import pow


class Hillas:
	def __init__(self, x_pmt, y_pmt, amp):
		assert len(x_pmt)==len(y_pmt)==len(amp), "not equal amount of coordinates and amplitudes"


		self.M00 = 0
		self.M10 = 0
		self.M01 = 0
		self.M11 = 0
		self.M20 = 0
		self.M02 = 0

		for i in range(len(amp)):
			self.M00 += amp[i]								 # dimensionless
			self.M10 += amp[i]*x_pmt[i]                      # mm
			self.M01 += amp[i]*y_pmt[i]                      # mm
			self.M11 += amp[i]*x_pmt[i]*y_pmt[i]             # mm^2
			self.M20 += amp[i]*x_pmt[i]*x_pmt[i]             # mm^2
			self.M02 += amp[i]*y_pmt[i]*y_pmt[i]             # mm^2

		self.x_mean = self.M10/self.M00                      	# mm
		self.y_mean = self.M01/self.M00							# mm

		self.x_2_mean = self.M20/self.M00						# mm^2
		self.y_2_mean = self.M02/self.M00						# mm^2
		self.xy_mean = self.M11/self.M00						# mm^2

		self.sigma_x_2 = self.x_2_mean - self.x_mean*self.x_mean   # mm^2
		self.sigma_y_2 = self.y_2_mean - self.y_mean*self.y_mean   # mm^2
		self.sigma_xy = self.xy_mean - self.x_mean*self.y_mean     # mm^2

		self.d = self.sigma_y_2 - self.sigma_x_2					# mm^2
		self.z = sqrt(self.d*self.d + 4.*self.sigma_xy*self.sigma_xy)			# mm^2

		self.length = sqrt((self.sigma_x_2 + self.sigma_y_2 + self.z)/2.)  # mm
		self.width = sqrt((self.sigma_x_2 + self.sigma_y_2 - self.z)/2.)   # mm

		self.distance = sqrt(self.x_mean*self.x_mean + self.y_mean*self.y_mean)  # mm

		self.azwidth = sqrt((self.x_mean*self.x_mean*self.y_2_mean + self.y_mean*self.y_mean*self.x_2_mean - 2*self.x_mean*self.y_mean*self.xy_mean)/(self.distance*self.distance))  # mm

		self.u = 1 + self.d/self.z   # dimensionless

		self.v = 2 - self.u  # dimensionless
 
		self.miss = sqrt(0.5*(self.u*self.x_mean*self.x_mean + self.v*self.y_mean*self.y_mean) - (2*self.sigma_xy*self.x_mean*self.y_mean/self.z))  # mm

		self.alpha = asin(self.miss/self.distance)  # radian