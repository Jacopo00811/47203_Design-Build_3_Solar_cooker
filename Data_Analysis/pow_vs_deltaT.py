import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Defining variables
m = .175
lowess = sm.nonparametric.lowess

# Importing data
dataset=np.genfromtxt(fname = 'ExpData_SolarCooker_DesignBuild3.lvm', skip_header = 22 )
c_data = np.genfromtxt( fname= 'Specific_heat_of_water.csv', skip_header= 1, delimiter= ',')

# Defining functions
def c_of_T(TempX, c_data):
    res = np.array([])
    for i in TempX: 
        index = 0
        val = abs(i-c_data[0][0])
        for j in range(1,len(c_data)):
            diff = abs(i-c_data[j][0])
            if diff < val:
                val = diff
                index = j
        res = np.append(res, c_data[index][1])
    return res  

# Turning columns from lvm file into arrays
time =[row[0] for row in dataset]
Temp1 = [row[1] for row in dataset]
Temp2 = [row[3] for row in dataset]
Temp3 = [row[5] for row in dataset]
Temp4 = [row[7] for row in dataset]
Tr = [row[9] for row in dataset]
Temp6 = [row[11] for row in dataset]
Temp7 = [row[13] for row in dataset]


# Calculating Delta_T = Tw-Tr
Matrix = np.array([Temp1, Temp2, Temp3, Temp4, Temp6, Temp7])
Tw = np.mean(Matrix, axis=0)
Tfinal = np.subtract(Tw, Tr)

# Differentiating 
dTdt= np.gradient(Tw, time)


# Calculating Power
P=m*c_of_T(Tw, c_data)*dTdt

# Smoothing
delta_T_smooth, P_smooth = lowess(P, Tfinal, frac=0.1, return_sorted=True).T

# Fitting a line
a, b = np.polyfit(delta_T_smooth, P_smooth, 1)

# Plotting 
plt.plot(delta_T_smooth, P_smooth, 'r-', lw=3)
plt.plot(delta_T_smooth, a*delta_T_smooth+b, 'b--', label='Best Fit')
plt.xlabel('$\Delta$T ($\degree$C)', fontsize = 'large')
plt.ylabel('Power W', fontsize = 'large')
plt.title('Power vs. $\Delta$-Temperature Provided Data', fontsize = 'large')
plt.text(1, 35, 'y = ' + '{:.2f}'.format(b) + '{:.2f}'.format(a) + 'x', size=10, color = 'b')
plt.grid(color='black', linestyle='-', linewidth = 0.2)
plt.legend()
plt.show()