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
	"class that contains all events"
	s_pmt = 30.                               # mm
	all_row_column_pairs = set([(-12, 4), (8, -9), (0, -13), (8, 0), (0, -4), (11, -4), (8, 9), (-8, -8), (11, 5), (0, 5), (-8, 1), (-11, -5), (12, -3), (4, -7), (-11, 4), (4, 2), (3, 6), (-7, -8), (-5, 11), (-4, -6), (7, -6), (-4, 3), (7, 3), (8, -5), (0, -9), (8, 4), (0, 0), (11, 0), (-8, -4), (0, 9), (-8, 5), (3, 1), (3, 10), (-5, 6), (-4, -11), (-4, -1), (-4, -2), (7, -2), (-12, -6), (7, -1), (-4, 7), (7, 7), (-12, 3), (0, -5), (11, -5), (-8, -9), (11, 4), (-8, 0), (10, 8), (3, -4), (-5, -8), (3, 5), (-5, 1), (-5, 10), (-4, -7), (7, -7), (-4, 2), (7, 2), (-12, -1), (-12, -2), (-12, 7), (0, -10), (-8, -5), (10, 3), (2, 8), (-9, 8), (3, -9), (3, 0), (-5, -4), (3, 9), (-5, 5), (-4, -3), (7, -3), (-12, -7), (-12, 2), (6, 10), (-13, 6), (-2, 6), (-1, 6), (10, -2), (10, -1), (2, -6), (-9, -6), (10, 7), (-9, 3), (2, 3), (2, 12), (3, -5), (-5, -9), (3, 4), (-5, 0), (-5, 9), (7, -8), (6, -4), (6, 5), (-1, 1), (-13, 1), (-2, 1), (-1, 10), (-2, 10), (-10, 6), (10, -7), (2, -11), (10, 2), (2, -2), (-9, -2), (-9, -1), (2, -1), (-9, 7), (2, 7), (3, -10), (-5, -5), (9, -3), (-6, 8), (5, 8), (9, 6), (6, -9), (6, 0), (-13, -4), (-1, -4), (-2, -4), (-10, -8), (6, 9), (-13, 5), (-2, 5), (-1, 5), (-10, 1), (10, -3), (2, -7), (-9, -7), (10, 6), (-9, 2), (2, 2), (2, 11), (-5, -10), (-6, -6), (9, -8), (-6, 3), (5, 3), (9, 1), (-3, 8), (6, -5), (-1, -9), (-2, -9), (6, 4), (-2, 0), (-13, 0), (-1, 0), (-10, -4), (-2, 9), (-1, 9), (-10, 5), (10, -8), (2, -12), (2, -3), (-9, -3), (13, -6), (13, 3), (1, 10), (-7, 6), (-6, -2), (-6, -1), (5, -2), (-3, -6), (5, -1), (-6, 7), (5, 7), (9, -4), (-3, 3), (9, 5), (-3, 12), (6, -10), (-2, -5), (-13, -5), (-1, -5), (-13, 4), (-1, 4), (-2, 4), (-10, 0), (12, 6), (2, -8), (4, 11), (1, -4), (13, -2), (13, -1), (13, 7), (1, 5), (-7, 1), (-7, 10), (5, -7), (-6, -7), (-3, -11), (5, 2), (-6, 2), (-3, -2), (-3, -1), (5, 11), (9, 0), (-3, 7), (9, 9), (6, -6), (-1, -10), (-2, -10), (-10, -5), (-10, 4), (12, 1), (4, -3), (-11, 8), (4, 6), (1, -9), (1, 0), (13, 2), (-7, -4), (1, 9), (-7, 5), (5, -3), (-6, -3), (-3, -7), (9, -5), (-6, 6), (5, 6), (-3, 2), (-3, 11), (8, 8), (0, 4), (0, 13), (-8, 9), (-11, -6), (12, -4), (4, -8), (-11, 3), (12, 5), (4, 1), (4, 10), (1, -5), (13, -3), (-7, -9), (1, 4), (-7, 0), (1, 13), (-7, 9), (5, -8), (-4, 11), (-6, -8), (-3, -3), (8, -6), (8, 3), (0, 8), (11, 8), (-8, 4), (-11, -1), (-11, -2), (12, 0), (4, -4), (-11, 7), (4, 5), (1, -10), (-7, -5), (-7, 4), (-4, 6), (7, 6), (-3, -8), (8, -2), (8, -1), (0, -6), (11, -6), (8, 7), (0, 3), (11, 3), (0, 12), (-8, 8), (-11, -7), (12, -5), (4, -9), (-11, 2), (12, 4), (4, 0), (4, 9), (1, -6), (-4, -8), (7, 1), (-4, 1), (-12, -3), (-4, 10), (7, 10), (-12, 6), (8, -7), (0, -11), (8, 2), (0, -2), (0, -1), (11, -1), (-8, -6), (11, -2), (0, 7), (11, 7), (-8, 3), (-11, -3), (4, -5), (-11, 6), (3, 8), (-5, 4), (-4, -4), (7, -4), (-4, 5), (7, 5), (-12, 1), (8, -3), (0, -7), (11, -7), (0, 2), (11, 2), (-8, -1), (-8, -2), (-8, 7), (4, -10), (3, -6), (3, 3), (3, 12), (-5, 8), (-4, -9), (7, -9), (7, 0), (-4, 0), (-12, -4), (-4, 9), (7, 9), (-12, 5), (8, -8), (0, -12), (0, -3), (11, -3), (-8, -7), (-8, 2), (10, 1), (-9, 6), (2, 6), (7, 8), (3, -11), (3, -2), (3, -1), (-5, -6), (3, 7), (-5, 3), (-4, -5), (7, -5), (-4, 4), (7, 4), (-12, 0), (6, 8), (-1, 13), (10, -4), (-9, -8), (10, 5), (-9, 1), (2, 1), (2, 10), (3, -7), (3, 2), (-5, -2), (-5, -1), (3, 11), (-5, 7), (-4, -10), (-12, -5), (6, 3), (-1, 8), (-2, 8), (10, 0), (2, -4), (-9, -4), (-9, 5), (2, 5), (3, -3), (-5, -7), (-5, 2), (9, 4), (6, -2), (6, -1), (-2, -6), (-1, -6), (-13, -6), (6, 7), (-13, 3), (-1, 3), (-2, 3), (-2, 12), (-1, 12), (-10, 8), (10, -5), (2, -9), (10, 4), (-9, 0), (2, 0), (2, 9), (-9, 9), (13, 6), (3, -8), (-5, -3), (5, 1), (-6, 1), (5, 10), (-6, 10), (9, 8), (-3, 6), (6, -7), (-1, -11), (-2, -11), (6, 2), (-2, -2), (-1, -2), (-13, -2), (-10, -6), (-13, -1), (-13, 7), (-2, -1), (-1, -1), (-10, 3), (-2, 7), (-1, 7), (2, -5), (-9, -5), (2, 4), (-9, 4), (13, 1), (1, 8), (5, -4), (-6, -4), (9, -6), (-6, 5), (5, 5), (-3, 1), (9, 3), (-3, 10), (6, -3), (-1, -7), (-2, -7), (6, 6), (-13, 2), (-2, 2), (-1, 2), (-10, -2), (-10, -1), (-1, 11), (-2, 11), (-10, 7), (10, -6), (2, -10), (13, -4), (1, 3), (13, 5), (1, 12), (-7, 8), (5, -9), (-6, -9), (-6, 0), (5, 0), (-3, -4), (9, -2), (-6, 9), (5, 9), (9, -1), (-3, 5), (9, 7), (6, -8), (-1, -12), (-2, -12), (6, 1), (-2, -3), (-13, -3), (-1, -3), (-10, -7), (-10, 2), (4, 4), (1, -11), (1, -2), (1, -1), (13, 0), (-7, -6), (1, 7), (-7, 3), (5, -5), (-6, -5), (-3, -9), (9, -7), (-6, 4), (5, 4), (-3, 0), (9, 2), (-3, 9), (8, 6), (-1, -8), (-2, -8), (0, 11), (-10, -3), (12, -6), (-11, 1), (12, 3), (4, 8), (1, -7), (13, -5), (1, 2), (13, 4), (-7, -2), (-7, -1), (1, 11), (-7, 7), (5, -10), (-6, -10), (-3, -5), (-3, 4), (8, 1), (11, 6), (0, 6), (-11, -4), (12, -2), (12, -1), (4, -6), (-11, 5), (12, 7), (4, 3), (1, -12), (1, -3), (-7, -7), (1, 6), (-7, 2), (5, -6), (-3, -10), (8, -4), (0, -8), (8, 5), (0, 1), (11, 1), (-8, -3), (0, 10), (-8, 6), (12, -7), (4, -11), (-11, 0), (12, 2), (4, -1), (4, -2), (4, 7), (1, -8), (1, 1), (-7, -3), (-4, 8)])
	all_x_y_pairs = [[float("Nan") for i in range(27)] for j in range(27)]

	def _init_x_y_pairs(self):
		for pair in sorted(self.all_row_column_pairs):
			x = self.s_pmt/2. * (2.*float(pair[1]) - float(pair[0]&1))
			y = float(pair[0])*self.s_pmt*sin(60.*pi/180)
			self.all_x_y_pairs[pair[0]][pair[1]] = (x, y)


	def __init__(self, file_name):
		# 1 dimensional arrays
		self.file_name = file_name
		self._init_x_y_pairs()
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
		self.row_column_pairs =[]
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
		""" adding new events headers to the class """
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
			self.particle_type.append("unknown particle (not 1, 14 or 5626)")
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
		self.row_column_pairs.append([])
		self.x_pmt.append([])
		self.y_pmt.append([])
		self.amplitudes.append([])
		self.avg_times.append([])
		self.std_times.append([])
		

	def add_pixel(self, row_number, column_number, amplitude, average_time, std_time):
		""" adding activated pixel info to the latest added event """
		self.row_numbers[-1].append(row_number)
		self.column_numbers[-1].append(column_number)
		self.row_column_pairs[-1].append((row_number, column_number))
		self.amplitudes[-1].append(amplitude)
		self.avg_times[-1].append(average_time)
		self.std_times[-1].append(std_time)
		x = self.s_pmt/2. * (2.*float(row_number) - float(column_number&1))
		y = float(column_number)*self.s_pmt*sin(60.*pi/180)
		self.x_pmt[-1].append(x)
		self.y_pmt[-1].append(y)


	def draw_event(self, n):
		print('\n\nevent number:', n, " is drawing")
		print("e's in event:", self.N_photoelectrons[n])
		print("activated pixels number:", self.N_pixels[n])
		print("particle:", self.particle_type[n])
		print("primary energy:", "{:.2f} GeV".format(self.energy[n]*1e-9))
		print("distance from core:", self.distance[n], 'm\n\n') 

		fig, ax = plt.subplots()
		patches = []
		alphas = []           # self.amplitudes[n]

		max_amp = np.array(self.amplitudes[n]).max()

		for pair in self.all_row_column_pairs:
			if pair in self.row_column_pairs[n]:
				ind = self.row_column_pairs[n].index(pair)
				patches.append(mpatches.RegularPolygon(self.all_x_y_pairs[pair[0]][pair[1]], 6, 10*np.sqrt(3)))
				alphas.append(self.amplitudes[n][ind])
			else:
				patches.append(mpatches.RegularPolygon(self.all_x_y_pairs[pair[0]][pair[1]], 6, 10*np.sqrt(3)))
				alphas.append(-0.5*max_amp)


		norm = plt.Normalize(-0.5*np.array(alphas).max(), np.array(alphas).max())  # np.array(alphas).min()
		self.pixels = PatchCollection(patches, cmap="inferno", norm=norm, match_original = True) 

		self.pixels.set_array(alphas)


		polys = ax.add_collection(self.pixels)

		plt.xticks(np.arange(-420, 435, step=60))   
		plt.yticks(np.arange(-225*sqrt(3), 240*sqrt(3), step=15*sqrt(3)))  
		ax.set_title('Event №' + str(n) + ', ' + self.particle_type[n] + ', E =' + "{:.2f}".format(self.energy[n]*1e-9) + ' GeV', fontsize=18)
		plt.xlabel('x [mm]', fontsize=14)   
		plt.ylabel('y [mm]', fontsize=14)   
		fig.colorbar(polys)   # , cmap="rainbow"	    
		ax.axis('equal')
		plt.grid(True, which='both')
		plt.savefig("images/"+self.file_name + "/events/event_" +str(n)+".svg")
		plt.show()


	def enable_pixel_picker(self):
		"""enable ability to click on pixels"""
		print('enabling pixel clicking')

		self.pixels.set_picker(True)
		self.pixels.set_pickradius(5*sqrt(3))
