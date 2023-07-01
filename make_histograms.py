#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

seed = 42
rng = np.random.default_rng(seed)
#size << " " << length << " " << width << " " << dist 

size_gamma = []
length_gamma = []
width_gamma = []
distt_gamma = []

with open("hillas_txt/hillas_gamma_0.txt") as file:
    for line in file.readlines():
        line = line.split()
            
        size_gamma.append(float(line[0]))
        length_gamma.append(float(line[1]))
        width_gamma.append(float(line[2]))
        distt_gamma.append(float(line[3]))
            
size_gamma = np.array(size_gamma)
length_gamma = np.array(length_gamma)
width_gamma = np.array(width_gamma)
distt_gamma = np.array(distt_gamma)




    #print("size: ", size.mean(), "  ", size.std(), "   shape: ", size.shape)          # 783.0082182111526    1993.3876005949087    size:  (79336,)
    #print("length: ", length.mean(), "  ", length.std(), "   shape: ", length.shape)  # 0.38131820985933246  0.0903902460062103    size:  (79336,)
    #print("width: ", width.mean(), "  ", width.std(), "   shape: ", width.shape)         # 0.14379249117424628  0.03776552676808203   size:  (79336,)
    #print("distt: ", distt.mean(), "  ", distt.std(), "   shape: ", distt.shape)      # 2.0975326469799334   0.5178436596505122    size:  (79336,)

#gamma_dataset = np.stack((size, length, width, distt), axis=0)
#print(gamma_dataset.shape)  # shape: (4, 79336)
#gamma_labels = np.ones(gamma_dataset.shape[1])


size_proton = []
length_proton = []
width_proton = []
distt_proton = []

with open("hillas_txt/hillas_proton_0.txt") as file:
    for line in file.readlines():
        line = line.split()
        
        size_proton.append(float(line[0]))
        length_proton.append(float(line[1]))
        width_proton.append(float(line[2]))
        distt_proton.append(float(line[3]))
size_proton = np.array(size_proton)
length_proton = np.array(length_proton)
width_proton = np.array(width_proton)
distt_proton = np.array(distt_proton)


fig, ax = plt.subplots()

#x = np.concatenate((size_gamma.reshape(len(size_gamma), 1), size_proton.reshape(len(size_proton), 1)), axis=1)
x = [width_gamma, width_proton]
#x = [distt_gamma, distt_proton]
#x = [distt_gamma, distt_proton]
#x = [distt_gamma, distt_proton]
labels = ['gamma', 'proton']

ax.hist(x, 100, density=False, histtype='step', stacked=False, label=labels)          
ax.legend(prop={'size': 20})
ax.set_title("Width", fontsize=60)
ax.set_yscale('log')
plt.grid(True, axis='y')
#plt.savefig("hillas_plots/size_hist.pdf")
plt.show()

exit()