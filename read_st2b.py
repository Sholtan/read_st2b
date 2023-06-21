#!/usr/bin/env python3

import struct
from st2b_event_class import Event
import numpy as np
import matplotlib.pyplot as plt

file_name = "st2b/taiga607_st2b_1"

header_size = 180                # 4 ints + 8 doubles + 1 int
pixel_amplitude_size = 28   # 3 ints + 2 doubles

event_counter = 0

events_list = []


#energy_list = []
#ev_els = []
#x_offset_list = []
#y_offset_list = []
#x_telescope_list = []
#x_core_list = []
#y_core_list = []
#z_core_list = []

list_to_draw = [[], [], [], [], [], [], [], []]

with open(file_name, "rb") as file_in_bytes:
	header_chunk = file_in_bytes.read(header_size)


	while header_chunk:
		N_run, N_scattering, N_telescope, N_photoelectrons = struct.unpack('<4i', header_chunk[0:16])   
		energy, theta, phi, x_core, y_core, z_core, h_1st_interaction, particle_type, xmax, hmax, x_telescope, y_telescope, z_telescope, x_offset, y_offset, theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average = struct.unpack('<20d', header_chunk[16:176])
		N_pixels, = struct.unpack('<i', header_chunk[176:180])
		some_event = Event(N_run, N_scattering, N_telescope, N_photoelectrons, 
			energy, theta, phi, x_core, y_core, z_core, 
			h_1st_interaction, particle_type, xmax, hmax, 
			x_telescope, y_telescope, z_telescope, x_offset, y_offset, 
			theta_telescope, phi_telescope, delta_alpha, alpha_pmt, T_average)


		for i in range(N_pixels):
			pixel_chunk = file_in_bytes.read(pixel_amplitude_size)
			amplitude, row_number, column_number = struct.unpack('<3i', pixel_chunk[0:12])

			

			average_time, std_time = struct.unpack('<2d', pixel_chunk[12:28])

			some_event.add_pixel(row_number, column_number, amplitude, average_time, std_time)
		#print(some_event.pixel_row_column_amp_avgtime_stdtime)

		events_list.append(some_event)
		event_counter+=1
		if event_counter%100==0:
			print("event: ", event_counter)
		
		header_chunk = file_in_bytes.read(header_size)

print("WHILE DONE")
print("len(events_list): ", len(events_list), "\n\n")




for i in range(len(events_list)):
	#if events_list[i].N_photoelectrons>=50:
		#ev_els.append(events_list[i].N_photoelectrons)
	list_to_draw[0].append(events_list[i].energy)
	list_to_draw[1].append(events_list[i].N_photoelectrons)
	list_to_draw[2].append(events_list[i].x_offset)
	list_to_draw[3].append(events_list[i].y_offset)
	list_to_draw[4].append(events_list[i].x_telescope)
	list_to_draw[5].append(events_list[i].x_core)
	list_to_draw[6].append(events_list[i].y_core)
	list_to_draw[7].append(events_list[i].z_core)
	

#ev_els = np.array(ev_els)
#x_offset_list = np.array(x_offset_list)
#y_offset_list = np.array(y_offset_list)
#x_telescope_list = np.array(x_telescope_list)
#x_core_list = np.array(x_core_list)
#y_core_list = np.array(y_core_list)
#z_core_list = np.array(z_core_list)
#energy_list = np.array(energy_list)


fig, ax = plt.subplots(2, 4)


print(ax)



for i in range(2):
	for j in range(4):
		ax[i, j].hist(list_to_draw[i*4+j], 100)
		ax[i, j].set_title(str(i*4+j))

#ax.hist(list_to_draw[7], 100)
#ax.set_title("1")







plt.show()
input("pause\n")





#for i in range(51):
	#print(events_list[i].N_photoelectrons)

	
		
		
		




'''
		print("N_run: ", N_run, "   ", end=' ')
		print("N_run: ", type(N_run))
		print("N_scattering: ", N_scattering, "   ", end=' ')
		print("N_scattering: ", type(N_scattering))
		print("N_telescope: ", N_telescope, "   ", end=' ')
		print("N_telescope: ", type(N_telescope))
		print("N_photoelectrons: ", N_photoelectrons, "   ", end=' ')
		print("N_photoelectrons: ", type(N_photoelectrons))
		print("energy: ", energy, "   ", end=' ')
		print("energy: ", type(energy))
		print("theta: ", theta, "   ", end=' ')
		print("theta: ", type(theta))
		print("phi: ", phi, "   ", end=' ')
		print("phi: ", type(phi))
		print("N_run: ", x_core, "   ", end=' ')
		print("N_run: ", type(x_core))
		print("N_run: ", y_core, "   ", end=' ')
		print("N_run: ", type(y_core))
		print("N_run: ", z_core, "   ", end=' ')
		print("N_run: ", type(z_core))
		print("N_run: ", h_1st_interaction, "   ", end=' ')
		print("N_run: ", type(h_1st_interaction))
		print("N_run: ", particle_type, "   ", end=' ')
		print("N_run: ", type(particle_type))
		print("N_run: ", xmax, "   ", end=' ')
		print("N_run: ", type(xmax))
		print("N_run: ", hmax, "   ", end=' ')
		print("N_run: ", type(hmax))
		print("N_run: ", x_telescope, "   ", end=' ')
		print("N_run: ", type(x_telescope))
		print("N_run: ", y_telescope, "   ", end=' ')
		print("N_run: ", type(y_telescope))
		print("N_run: ", z_telescope, "   ", end=' ')
		print("N_run: ", type(z_telescope))
		print("N_run: ", x_offset, "   ", end=' ')
		print("N_run: ", type(x_offset))
		print("N_run: ", y_offset, "   ", end=' ')
		print("N_run: ", type(y_offset))
		print("N_run: ", theta_telescope, "   ", end=' ')
		print("N_run: ", type(theta_telescope))
		print("N_run: ", phi_telescope, "   ", end=' ')
		print("N_run: ", type(phi_telescope))
		print("N_run: ", delta_alpha, "   ", end=' ')
		print("N_run: ", type(delta_alpha))
		print("N_run: ", alpha_pmt, "   ", end=' ')
		print("N_run: ", type(alpha_pmt))
		print("N_run: ", T_average, "   ", end=' ')
		print("N_run: ", type(T_average))
		print("N_pixels: ", N_pixels, "   ", end=' ')
		print("N_pixels: ", type(N_pixels))'''