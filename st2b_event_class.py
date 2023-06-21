#!/usr/bin/env python3

import numpy as np
from math import sin
from math import pi

class Event:
	s_pmt = 3.
	def __init__(self, N_run, N_scattering, N_telescope, N_photoelectrons, 
		energy, theta, phi, x_core, y_core, z_core, 
		h_1st_interaction, particle_type, xmax, hmax, 
		x_telescope, y_telescope, z_telescope, x_offset, y_offset, 
		theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average):
		self.N_run = N_run
		self.N_scattering = N_scattering
		self.N_telescope = N_telescope
		self.N_photoelectrons = N_photoelectrons


		self.energy = energy
		self.theta = theta
		self.phi = phi
		self.x_core = x_core
		self.y_core = y_core

		self.z_core = z_core
		self.h_1st_interaction = h_1st_interaction
		
		if (particle_type == 1):
			self.particle_type = "gamma"
		elif particle_type == 14:
			self.particle_type = "proton"
		elif particle_type == 5626:
			self.particle_type == iron
		else:
			print("particle is not 1, 14, 5626 !!!")


		self.xmax = xmax
		self.hmax = hmax
		self.x_telescope = x_telescope
		self.y_telescope = y_telescope
		self.z_telescope = z_telescope
		self.x_offset = x_offset
		self.y_offset = y_offset

		self.x_core_minus_offset = x_core - x_offset
		self.x_core_minus_offset = y_core - y_offset

		self.theta_telescope = theta_telescope
		self.phi_telescope = phi_telescope
		self.delta_alpha = delta_alpha
		self.alpha_pmt = alpha_pmt
		self.T_average = T_average

		#self.pixel_row_column_amp_avgtime_stdtime = []
		self.row_numbers = []
		self.column_numbers = []
		self.x_pmt = []
		self.y_pmt = []
		self.amplitudes = []
		self.avg_times = []
		self.std_times = []
		#print("Event is created!!!")

	def add_pixel(self, row_number, column_number, amplitude, average_time, std_time):
		#self.pixel_row_column_amp_avgtime_stdtime.append(info)
		self.row_numbers.append(row_number)
		self.column_numbers.append(column_number)
		self.amplitudes.append(amplitude)
		self.avg_times.append(average_time)
		self.std_times.append(std_time)
		x = self.s_pmt/2. * (2.*float(column_number) - float(row_number&1))
		y = float(row_number)*self.s_pmt*sin(60.*pi/180)
		self.x_pmt.append(x)
		self.y_pmt.append(y)





