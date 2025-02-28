#A
import numpy as np
arr = np.array( [[ 1, 2, 3], [ 4, 2, 5]] )
print("Array is of type: ", type(arr))
print("No. of dimensions: ", arr.ndim)
print("Shape of array: ", arr.shape)
print("Size of array: ", arr.size)
print("Array stores elements of type: ", arr.dtype)

#B
import numpy as np
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
"Array type is complex:\n", d)
e = np.random.random((2, 2))
print ("\nA random array:\n", e)
f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)
g = np.linspace(0, 5, 10)
print ("\nA sequential array with 10 values between"
"0 and 5:\n", g)
arr = np.array([[1, 2, 3, 4], [5, 2, 4, 2], [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print ("\nOriginal array:\n", arr)
print ("Reshaped array:\n", newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()
print ("\nOriginal array:\n", arr)
print ("Fattened array:\n", flarr)

#C
import numpy as np
arr = np.array([[-1, 2, 0, 4],
[4, -0.5, 6, 0],
[2.6, 0, 7, 8],
[3, -7, 4, 2.0]])
temp = arr[:2, ::2]
print ("Array with first 2 rows and alternate"
"columns(0 and 2):\n", temp)
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
"(3, 0):\n", temp)
cond = arr > 0 
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)

#D
import numpy as np
a = np.array([1, 2, 5, 3])
print ("Adding 1 to every element:", a+1)
print ("Subtracting 3 from each element:", a-3)
print ("Multiplying each element by 10:", a*10)
print ("Squaring each element:", a**2)
a *= 2
print ("Doubled each element of original array:", a)
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)

#E
import numpy as np
a = np.array([[1, 2],
[3, 4]])
b = np.array([[5, 6],
[7, 8]])
print("Vertical stacking:\n", np.vstack((a, b)))
print("\nHorizontal stacking:\n", np.hstack((a, b)))
c = [5, 6]
print("\nColumn stacking:\n", np.column_stack((a, c)))
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))

#F
import numpy as np
a = np.array([[1, 3, 5, 7, 9, 11],
[2, 4, 6, 8, 10, 12]])
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 2))
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))