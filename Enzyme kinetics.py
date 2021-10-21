import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)
x = np.linspace(10**4, 10**5, 1001) #x = Thres. fluoroscence
a = 4 # a = QP(in mol) cut per unit mol Cas
b = 10000 # b = Fluoroscence prod by per unit mol QP
g = 1 # g = FG(in mol) cut per unit mol Cas
d = 10 #d = rate of production of FG by LAMP
p = 5 # p = mol of FG prod by 1 M FG
t = 10 #t = time taken to complete rxn
y = 5 #min FG
w = np.linspace(0,5,1000) #initial FG
mincas = x/(a*b)
minQP = x/b
tau = (y - w)/d
minFG = g*x*t/(a*b)
# plt.plot(tau, w)
plt.plot(x, minFG)
plt.xlabel('Threshold Frequency')
plt.ylabel('Minimum Free Gene')
plt.show() 
# print(tau)
# print(mincas, y, tau)
