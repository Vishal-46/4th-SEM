#1
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


x = np.linspace(0, 10, 100)
fig = plt.figure() 
plt.plot(x, np.sin(x), '-')  
plt.plot(x, np.cos(x), '--')  
plt.show() 

fig.savefig('my_figure.png')
from IPython.display import Image
Image('my_figure.png')


x = np.linspace(0, 10, 100) 
plt.figure() 
plt.subplot(2, 1, 1) 
plt.plot(x, np.sin(x))
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))  
plt.show()  