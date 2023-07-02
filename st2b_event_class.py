#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from math import sin
from math import pi
from math import sqrt
from math import pow

import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection

def draw_hist(some_list, title, file_name):
	fig, ax = plt.subplots()
	ax.hist(some_list)
	ax.set_title(title)
	plt.savefig("images/"+file_name+"/"+title+".svg")
	plt.show()


def draw_stats(all_events, file_name):
	draw_hist(all_events.energy, "energy", file_name)
	draw_hist(all_events.N_run, "N_run", file_name)
	draw_hist(all_events.N_scattering, "N_scattering", file_name)
	draw_hist(all_events.N_telescope, "N_telescope", file_name)
	draw_hist(all_events.N_photoelectrons, "N_photoelectrons", file_name)
	draw_hist(all_events.N_pixels, "N_pixels", file_name)
	draw_hist(all_events.theta, "theta", file_name)
	draw_hist(all_events.phi, "phi", file_name)
	draw_hist(all_events.x_core, "x_core", file_name)
	draw_hist(all_events.y_core, "y_core", file_name)
	draw_hist(all_events.z_core, "z_core", file_name)
	draw_hist(all_events.h_1st_interaction, "h_1st_interaction", file_name)
	draw_hist(all_events.particle_type, "particle_type", file_name)
	draw_hist(all_events.xmax, "xmax", file_name)
	draw_hist(all_events.hmax, "hmax", file_name)
	draw_hist(all_events.x_telescope, "x_telescope", file_name)
	draw_hist(all_events.y_telescope, "y_telescope", file_name)
	draw_hist(all_events.z_telescope, "z_telescope", file_name)
	draw_hist(all_events.x_offset, "x_offset", file_name)
	draw_hist(all_events.y_offset, "y_offset", file_name)
	draw_hist(all_events.theta_telescope, "theta_telescope", file_name)
	draw_hist(all_events.phi_telescope, "phi_telescope", file_name)
	draw_hist(all_events.delta_alpha, "delta_alpha", file_name)
	draw_hist(all_events.alpha_pmt, "alpha_pmt", file_name)
	draw_hist(all_events.T_average, "T_average", file_name)
	draw_hist(all_events.x_core_minus_offset, "x_core_minus_offset", file_name)
	draw_hist(all_events.y_core_minus_offset, "y_core_minus_offset", file_name)
	draw_hist(all_events.distance, "distance", file_name)




class Events:
	s_pmt = 30.                               # mm
	def __init__(self):
		# 1 dimensional arrays
		self.N_run = []                      # int32
		self.N_scattering = []               # int32
		self.N_telescope = []                # int32
		self.N_photoelectrons = []           # int32
		self.N_pixels = []           # int32

		
		self.energy = []                     # eV
		self.theta = []                      # radian
		self.phi = []                        # radian
		self.x_core = []                     # m
		self.y_core = []                     # m
		self.z_core = []                     # m
		self.h_1st_interaction = []          # m
		self.particle_type = []              # 
		self.xmax = []                       # g/cm^2
		self.hmax = []                       # m
		self.x_telescope = []                # m
		self.y_telescope = []                # m
		self.z_telescope = []                # m
		self.x_offset = []                   # m
		self.y_offset = []                   # m

		self.x_core_minus_offset = []        # m
		self.y_core_minus_offset = []        # m

		self.distance = []                   # m

		self.theta_telescope = []            # radian
		self.phi_telescope = []              # radian
		self.delta_alpha = []                # radian
		self.alpha_pmt = []                  # radian
		self.T_average = []                  # s
		self.row_numbers = []                # int32
		self.column_numbers = []             # int32
		self.x_pmt = [] 
		self.y_pmt = []
		self.amplitudes = []
		self.avg_times = []
		self.std_times = []


		# 2 dimensional arrays
		self.row_numbers = []
		self.column_numbers = []
		self.x_pmt = []                      # mm
		self.y_pmt = []                      # mm
		self.amplitudes = []                
		self.avg_times = []                  # s
		self.std_times = []                  # s

	def add_header(self, N_run, N_scattering, N_telescope, N_photoelectrons, 
		energy, theta, phi, x_core, y_core, z_core, 
		h_1st_interaction, particle_type, xmax, hmax, 
		x_telescope, y_telescope, z_telescope, x_offset, y_offset, 
		theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average, N_pixels):
		self.N_run.append(N_run)
		self.N_scattering.append(N_scattering)
		self.N_telescope.append(N_telescope)
		self.N_photoelectrons.append(N_photoelectrons)
		self.N_pixels.append(N_pixels)


		self.energy.append(energy)
		self.theta.append(theta)
		self.phi.append(phi)
		self.x_core.append(x_core * 0.001)
		self.y_core.append(y_core * 0.001)

		self.z_core.append(z_core * 0.001)
		self.h_1st_interaction.append(h_1st_interaction * 0.001)
		
		if (particle_type == 1):
			self.particle_type.append("gamma")
		elif particle_type == 14:
			self.particle_type.append("proton")
		elif particle_type == 5626:
			self.particle_type.append("iron")
		else:
			print("particle is not 1, 14, 5626 !!!")
		self.xmax.append(xmax)
		self.hmax.append(hmax * 0.001)
		self.x_telescope.append(x_telescope * 0.001)
		self.y_telescope.append(y_telescope * 0.001)
		self.z_telescope.append(z_telescope * 0.001)
		self.x_offset.append(x_offset * 0.001)
		self.y_offset.append(y_offset * 0.001)

		self.x_core_minus_offset.append(x_core * 0.001 - x_offset * 0.001)
		self.y_core_minus_offset.append(y_core * 0.001 - y_offset * 0.001)

		self.distance.append(sqrt(pow((x_core * 0.001 - x_offset * 0.001 - x_telescope * 0.001),2) + pow((y_core * 0.001 - y_offset * 0.001 - y_telescope * 0.001),2)))

		

		self.theta_telescope.append(theta_telescope)
		self.phi_telescope.append(phi_telescope)
		self.delta_alpha.append(delta_alpha)
		self.alpha_pmt.append(alpha_pmt)
		self.T_average.append(T_average)

		self.row_numbers.append([])
		self.column_numbers.append([])
		self.x_pmt.append([])
		self.y_pmt.append([])
		self.amplitudes.append([])
		self.avg_times.append([])
		self.std_times.append([])
		

	def add_pixel(self, row_number, column_number, amplitude, average_time, std_time):
		#self.pixel_row_column_amp_avgtime_stdtime.append(info)
		




		self.row_numbers[-1].append(row_number)
		self.column_numbers[-1].append(column_number)
		self.amplitudes[-1].append(amplitude)
		self.avg_times[-1].append(average_time)
		self.std_times[-1].append(std_time)
		x = self.s_pmt/2. * (2.*float(column_number) - float(row_number&1))
		y = float(row_number)*self.s_pmt*sin(60.*pi/180)
		self.x_pmt[-1].append(x)
		self.y_pmt[-1].append(y)


	def draw_event(self, n):
		print('event number:', n)
		print("e's in event:", self.N_photoelectrons[n])

		fig, ax = plt.subplots()
		patches = []
		alphas = self.amplitudes[n]



		for i in range(self.N_pixels[n]):
			patches.append(mpatches.RegularPolygon([self.x_pmt[n][i], self.y_pmt[n][i]], 6, 10*np.sqrt(3)))


		norm = plt.Normalize(np.array(alphas).min(), np.array(alphas).max())
		collection = PatchCollection(patches, cmap="rainbow", norm=norm, match_original = True) 

		collection.set_array(alphas)

		polys = ax.add_collection(collection)

		plt.xticks(np.arange(-440, 470, step=30))
		plt.yticks(np.arange(-400.730669589, 400.730669589, step=25.9807621135))

		fig.colorbar(polys)   # , cmap="rainbow"

		plt.show()

