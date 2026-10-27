#importing needed libraries
import numpy as np
import matplotlib.pyplot as plt
#import control as ct 

#variables 
t_data = np.array([0,5,10,20,30,50])
voltage = np.array([0.28,3.76,5.85,7.94,8.71,9.09])
voltage_0 = voltage[0]
voltage_1 = voltage[-1]
tau = 10
t = np.linspace(0,60,200)

#model 
voltage_c = voltage_1 - (voltage_1 - voltage_0)*np.exp(-t/tau)

#plot
plt.plot(t_data,voltage, lw = 1, ls = '', label = 'Measured',marker = 'o')
plt.plot(t,voltage_c, lw = 1, label = f'model tau = {tau} s', marker = '')
plt.grid(visible = True, axis = 'both',which = 'both')
plt.title('RC charging: measured vs model')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.savefig("circuit_models/RC_circuit/images/RC_tau.png")
plt.show()
