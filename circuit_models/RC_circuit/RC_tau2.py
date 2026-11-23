#import libraries for code
import numpy as np
import matplotlib.pyplot as plt
import control as ct 
#from scipy.optimize import curve_fit

#varibles 
R =  47e3
C = 470e-6
tau = R*C
#measured values
t_data = np.array([0,10,20,22,30,45,60,90,110])
voltage = np.array([0,3.385,5.535,5.950,6.860,7.880,8.405,8.775,8.88])
voltage_0 = voltage[0]
voltage_1 = voltage[-1]
v_s = 9.43
t = np.linspace(0,110,200)

#model
#voltage_c = voltage_1 - (voltage_1 - voltage_0)*np.exp(-t/tau)
#def charge_curve(time,V_f,tau):
#    return V_f * (1 - np.exp(-1/tau))
#fitted_vf, fitted_tau = curve_fit(charge_curve,t_data,voltage, p0 = [0,20])
#error = np.sqrt(np.diag(fitted_tau))
#print('fitted values: ', fitted_vf)
#print('Error: ', error)

num = [1]
dem =[tau, 1]
sys = ct.tf(num, dem)

#print(sys)
#print(ct.dcgain(sys))
#print(ct.poles(sys))
#print(ct.step_info(sys))

response = ct.step_response(sys, T=t)
v_sim = response.outputs * v_s


plt.figure(figsize=(8,4.5))
plt.plot(response.time,v_sim, label = f'Model ($\\tau = {tau:.2f}$) s', linewidth = 2)
plt.plot(t_data, voltage, label= 'Measured',ls='',marker='o')
#plt.plot(t,fitted_vf, color = 'red', ls ='--')
plt.axhline(v_s, color = 'gray', ls = '--', label = f'$v_s = {v_s}$ V')
plt.axvline(tau, color = 'green', ls = ':', label = f'$\\tau$ = {tau} s'  )
plt.grid(True,alpha = 0.3)

plt.title('First Order RC circuit Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Capacitor Voltage (V)')
plt.legend()
plt.savefig("circuit_models/RC_circuit/images/RC_tau2.png")
plt.show()


