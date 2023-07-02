#!/usr/bin/env python3

import struct
from st2b_event_class import Events
from st2b_event_class import draw_stats
from st2b_event_class import draw_hist
from hillas_class import Hillas
import numpy as np
import matplotlib.pyplot as plt

from math import sin
from math import pi
from math import sqrt
from math import pow

file_name = "taiga607_st2b_1"

header_size = 180                # 4 ints + 8 doubles + 1 int
pixel_amplitude_size = 28   # 3 ints + 2 doubles

event_counter = 0






all_events = Events()

list_to_draw = [[], [], [], [], [], [], [], [], []]

with open("st2b/"+file_name, "rb") as file_in_bytes:
	header_chunk = file_in_bytes.read(header_size)


	while header_chunk:
		N_run, N_scattering, N_telescope, N_photoelectrons = struct.unpack('<4i', header_chunk[0:16])   
		energy, theta, phi, x_core, y_core, z_core, h_1st_interaction, particle_type, xmax, hmax, x_telescope, y_telescope, z_telescope, x_offset, y_offset, theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average = struct.unpack('<20d', header_chunk[16:176])
		N_pixels, = struct.unpack('<i', header_chunk[176:180])
		all_events.add_header(N_run, N_scattering, N_telescope, N_photoelectrons, 
			energy, theta, phi, x_core, y_core, z_core, 
			h_1st_interaction, particle_type, xmax, hmax, 
			x_telescope, y_telescope, z_telescope, x_offset, y_offset, 
			theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average, N_pixels)

		#print("distance: ", sqrt(pow((x_core * 0.001 - x_offset * 0.001 - x_telescope * 0.001),2) + pow((y_core * 0.001 - y_offset * 0.001 - y_telescope * 0.001),2)))

		#if event_counter%20==0:
			#input("pause\n")


		for i in range(N_pixels):
			pixel_chunk = file_in_bytes.read(pixel_amplitude_size)
			amplitude, row_number, column_number = struct.unpack('<3i', pixel_chunk[0:12])

			

			average_time, std_time = struct.unpack('<2d', pixel_chunk[12:28])

			all_events.add_pixel(row_number, column_number, amplitude, average_time, std_time)
		#print(some_event.pixel_row_column_amp_avgtime_stdtime)

		
		event_counter+=1
		if event_counter%1000==0:
			print("event: ", event_counter)
		
		header_chunk = file_in_bytes.read(header_size)

print(file_name, " reading DONE")


#draw_stats(all_events, file_name)
draw_hist(all_events.N_pixels, "N_pixels", file_name)


print('e: ', all_events.N_photoelectrons[49])
print('n pix: ', all_events.N_pixels[49])
print('dist: ', all_events.distance[49])
print('len x: ', len(all_events.x_pmt[49]))
print('len y: ', len(all_events.y_pmt[49]))
print('len amp: ', len(all_events.amplitudes[49]))

first_hillas = Hillas(all_events.x_pmt[49], all_events.y_pmt[49], all_events.amplitudes[49])

print('x_mean ', first_hillas.x_mean)
print('y_mean ', first_hillas.y_mean)
print('length ', first_hillas.length)
print('width ', first_hillas.width)
print('distance ', first_hillas.distance)
print('azwidth ', first_hillas.azwidth)
print('miss ', first_hillas.miss)
print('alpha ', first_hillas.alpha/pi*180)


count = 0
acount = 0
print('ssssss')
for NN in all_events.N_pixels:
	if NN > 150:
		print('NN:', NN, ', event_number: ', count)
		all_events.draw_event(count)
		acount+=1
	if acount>20:
		break
	count+=1






