import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
a = 0.3 #
b = 0.2
c = 0.1
d = 0.1
f = 0.1
e = 0.02
g = 0.033
h = 0.047
mn = 0.99 #mortality of no diagnosis
ml = 0.6 #mortality of late diagnosis  
me = 0.3 #mortality of early diagnosis

def odes(x,t):
    S = x[0]
    In = x[1]
    Il = x[2]
    Ie = x[3]
    R = x[4]
    D = x[5]

    dSdt = -S*(a*In + b*Il + c*Ie) 
    dIndt = d*S*(a*In + b*Il + c*Ie)- e*In
    dIldt = f*S*(a*In + b*Il + c*Ie)- g*Il
    dIedt = (1-d-f)*S*(a*In + b*Il + c*Ie)- h*Ie
    dRdt = (1-mn)*e*In + (1-ml)*g*Il + (1-me)*h*Ie
    dDdt = mn*e*In + ml*g*Il + me*h*Ie

    return [dSdt, dIndt, dIldt, dIedt, dRdt, dDdt]
#define timescale and initial conditions
# 1 time unit = 30 days
t = np.linspace(1, 600, 600000)
x0 = [1-3*10**-6, 10**-6, 10**-6, 10**-6, 0, 0]
x = odeint(odes, x0, t)
S = x[:, 0]
In = x[:, 1]
Il = x[:, 2]
Ie = x[:,3]
R = x[:, 4]
D = x[:, 5]


# plt.plot(t, S, label = 'Susceptible')
plt.plot(t, Il, label = 'Late diagonised')
plt.plot(t, In, label = 'Not diagonised')
plt.plot(t, Ie, label = 'Early diagonised')
# plt.plot(t, R, label = 'Recovered')
# plt.plot(t, D, label= 'Deceased')
plt.legend()
plt.show()
print(S[-1], In[-1], Il[-1], Ie[-1], R[-1], D[-1])