import numpy as np
import matplotlib.pyplot as plt
###loading data
dataset=np.genfromtxt(fname = 'ExpData_SolarCooker_DesignBuild3.lvm', skip_header = 22)
X_Value=[row[0] for row in dataset]
Temp1 = [row[1] for row in dataset]
Temp2 = [row[3] for row in dataset]
Temp3 = [row[5] for row in dataset]
Temp4 = [row[7] for row in dataset]
Temp5 = [row[9] for row in dataset]
Temp6 = [row[11] for row in dataset]
Temp7 = [row[13] for row in dataset]

#Ploting dif temps

plt.plot(X_Value[:6973], Temp1[:6973], color = 'r', lw=1, label = 'Temp1')
plt.plot(X_Value[:6973], Temp2[:6973], color = 'b', lw=1, label = 'Temp2')
plt.plot(X_Value[:6973], Temp3[:6973], color = 'g', lw=1, label = 'Temp3')
plt.plot(X_Value[:6973], Temp2[:6973], color = 'y', lw=1, label = 'Temp2')
plt.plot(X_Value[:6973], Temp5[:6973], color = 'k', lw=1, label = 'Temp5')
plt.plot(X_Value[:6973], Temp6[:6973], color = 'm', lw=1, label = 'Temp6')
plt.plot(X_Value[:6973], Temp7[:6973], color = 'c', lw=1, label = 'Temp7')
plt.title('Temperature vs. Time Provided Data', fontsize = 'large')
plt.legend()
plt.xlabel('Time s', fontsize = 'large')
plt.ylabel('Temperature ($\degree$C)', fontsize = 'large')
plt.grid(color='black',linestyle='-', linewidth = 0.2)
plt.show()
#label axis, legned, units, gridlines

