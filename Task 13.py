print("\n\nQ1. (Basic Array Creation)")

# Importing NumPy library
import time
import numpy as np

# Creating a 1D array

array1 = np.array([10, 20, 30, 40, 50])

# Creating a 2D array

array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Displaying 1D array

print("1D Array:")
print(array1)

print("Shape :", array1.shape)

print("Data Type :", array1.dtype)

print()

# Displaying 2D array

print("2D Array:")
print(array2)

print("Shape :", array2.shape)

print("Data Type :", array2.dtype)

#=====================================================================================
#=====================================================================================

print("\n\nQ2. (np.zeros() and np.ones())")

# Creating arrays

array1 = np.zeros(8)

array2 = np.ones((4, 4))

array3 = np.zeros((3, 3))

# Displaying arrays

print("1D Array of 8 Zeros:")
print(array1)

print("\n4x4 Array of Ones:")
print(array2)

print("\n3x3 Matrix of Zeros:")
print(array3)

#=====================================================================================
#=====================================================================================

print("\n\nQ3. (np.arange())")

# Creating arrays using arange()

array1 = np.arange(0, 21, 1)

array2 = np.arange(10, 51, 2)

array3 = np.arange(5, 101, 5)

# Displaying arrays

print("Numbers from 0 to 20:")
print(array1)

print("\nEven Numbers from 10 to 50:")
print(array2)

print("\nNumbers from 5 to 100 with Step 5:")
print(array3)

#=====================================================================================
#=====================================================================================

print("\n\nQ4. (np.linspace())")

# Importing NumPy library

import numpy as np

# Creating arrays

array1 = np.linspace(0, 5, 10)

array2 = np.linspace(-10, 10, 15)

# Displaying arrays

print("10 Equally Spaced Numbers:")
print(array1)

print(f"Length : {len(array1)}")

print()

print("15 Equally Spaced Numbers:")
print(array2)

print(f"Length : {len(array2)}")

#=====================================================================================
#=====================================================================================

print("\n\nQ5. (Random Arrays)")

# Importing NumPy library

import numpy as np

# Generating random arrays

array1 = np.random.rand(10)

array2 = np.random.randn(3, 3)

array3 = np.random.randint(10, 51, (4, 5))

# Displaying arrays

print("Random Numbers Between 0 and 1:")
print(array1)

print("\n3x3 Standard Normal Distribution Matrix:")
print(array2)

print("\nRandom Integers Between 10 and 50:")
print(array3)

#=====================================================================================
#=====================================================================================

print("\n\nQ6. (Vectors and Basic Operations)")

#creating 2 vectors
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

#displaying the vectors:
print(f"Vector 1: {v1}\nVector 2: {v2}")

#Performing Operations 
print(f"\nAddition of the vectors:\n {v1+v2}")
print(f"\nSubtraction of the vectors:\n {v1-v2}")
print(f"\nElement-wise multiplication of the vectors:\n {v1*v2}")
print(f"\nDot product of the vectors: \n {np.dot(v1, v2)}")

#=====================================================================================
#=====================================================================================

print("\n\nQ7. (Matrices and Operations)")

#Creating arrays:
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

#Displaying initials:
print(f"Initial Matrices:\nA = {A}\nB = {B}")

#Performing Operation:
print(f"\nMatrix Addition:\n{A+B}")
print(f"\nMatrix multiplication or Dot Product:\n{A@B}")
print(f"\nElement-wise multiplication:\n{A*B}")

#=====================================================================================
#=====================================================================================

print("\n\nQ8. (Properties of Arrays)")

#Creating array of random integers
arr1 = np.random.randint(1, 100, (4, 4))

#Displaying Section:
print(f"Array:\n{arr1}")
print(f"\nShape: {arr1.shape}\n\nDimension: {arr1.ndim}\n\nTotal number of elements: {arr1.size}\n\nDatatype: {arr1.dtype}\n\nMinimum Value: {arr1.min()}\n\nMaximum Value: {arr1.max()}")


#=====================================================================================
#=====================================================================================

print("\n\nQ9. (Combined - Random + Reshape + Statistics)")

# Generating 20 random integers between 1 and 49
a = np.random.randint(1, 50, 20)

# Displaying the original 1D array
print(f"Initial Array:\n{a}")

# Reshaping the array into a 4x5 matrix
b = a.reshape(4, 5)

# Displaying the reshaped matrix
print(f"\nReshaping the array into 4x5 matrix:\n{b} ")

# Displaying sum and mean
print(f"Sum: {np.sum(a)}\nMean: {np.mean(b)}")

# Displaying standard deviation
print(f"Standard Deviation: {np.std(b)}")

# Displaying maximum value from each row
print(f"Maximum value in each row : {np.max(b, axis=1)}")

#=====================================================================================
#=====================================================================================

print("\n\nQ10. (Mini Project - NumPy Application)")

#Asking the user how many numbers they want to generate...
n = int(input("Enter the number of elements you want in the array:"))

#Creating  array...
print("\nCreating Your array Please wait...")

# Using time.sleep() to delay the output on the screen
time.sleep(2)

#Creating  array...
a = np.random.randint(10, 101, n)

#Displaying the array:
print(f"\nHere's The array you asked for:\n{a}")

#Displaying the array details:
print(f"\nMean of the array: {np.mean(a)}")
print(f"\nMedian of the array: {np.median(a)}")
print(f"\nSandard deviation of the array: {np.std(a)}")
print("\nReshaping the array...")

# Using time.sleep() to delay the output on the screen
time.sleep(2)

# Reshaping the array if possible
if n % 2 == 0:
    b = a.reshape(2, n // 2)
    print(f"\nThe reshaped array is here:\n{b}")  
    print(f"\nAnd... Here's its row-wise Sum: {np.sum(b, axis=1)}")

else:
    print(f"\nCan't reshape Your array! Here's the original one:\n{a}")