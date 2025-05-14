import matplotlib.pyplot as plt        
plt.style.use('seaborn-v0_8-whitegrid')        
import numpy as np        
fig = plt.figure()        
ax = plt.axes()        
x = np.linspace(0, 10, 1000)        
ax.plot(x, np.sin(x))
plt.plot()