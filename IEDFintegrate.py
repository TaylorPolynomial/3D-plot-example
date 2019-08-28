import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

### Create a file path to the destination containing

IEDF_DATA_PATH = '~/Microthrusters/IEDF/Energyprofile3D.csv'
six = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [1])
eight = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [2])
ten = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [3])
twenty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [4])
fourty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [5])
fifty = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [6])
x_axis = pd.read_csv(IEDF_DATA_PATH, header = 0, usecols = [0])

six = np.array(six)
eight = np.array(eight)
ten = np.array(ten)
twenty = np.array(twenty)
fourty = np.array(fourty)
fifty = np.array(fifty)
#x_axis = np.array(x_axis)
#x_axis = np.reshape(x_axis(1,250))
#x = np.linspace(1,250,250)
#x = np.stack(x, axis=0)
#z = np.linspace(1,74,250)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111, projection='3d')

z1 = np.linspace(6,6,250)
z2 = np.linspace(8,8,250)
z3 = np.linspace(10,10,250)
z4 = np.linspace(27,27,250)
z5 = np.linspace(40,40,250)
z6 = np.linspace(54,54,250)

#ax.set_xlabel('Energy [eV]',fontsize=10, )
#ax.set_zlabel('Probability')
#ax.set_ylabel('Applied voltage frequency [MHz]',rotation=90)

ax.plot(x_axis,z1,six.flatten(),label='6 MHz')
ax.plot(x_axis,z2,eight.flatten(),label='8 MHz')
ax.plot(x_axis,z3,ten.flatten(),label='10 MHz')
ax.plot(x_axis,z4,twenty.flatten(),label='27.12 MHz')
ax.plot(x_axis,z5,fourty.flatten(),label='40.68 MHz')
ax.plot(x_axis,z6,fifty.flatten(),label='54.24 MHz')

ax.legend(loc='upper center')

#ax.plot(x_axis,eight)
#ax.plot(x_axis,ten)
#ax.plot(x_axis,twenty)
#ax.plot(x_axis,fourty)
#ax.plot(x_axis,fifty)