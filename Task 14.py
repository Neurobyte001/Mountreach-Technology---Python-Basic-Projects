#importing numpy
import numpy as np

print("\nQ1. (Array Properties)")

#Creating a 2D array
a = np.random.randint(10, 100, (5, 6))

#displaying the initial array:
print(f"\nThe initial array: \n{a}")  

#displaying the array details:
print(f"\nShape of the array: {a.shape}")

print(f"\nTotal Number of elements: {a.size}")

print(f"\nDatatype: {a.dtype}")

#=====================================================================
#=====================================================================

print("\n\nQ2. (Statistical Methods - Basic)")

# Creating random array
a = np.random.randint(1, 51, 20)

print("Array:\n", a)

# Displaying statistics
print("\nMinimum Value :", np.min(a))
print("Index of Minimum :", np.argmin(a))

print("\nMaximum Value :", np.max(a))
print("Index of Maximum :", np.argmax(a))

print("\nSum :", np.sum(a))
print("Mean :", np.mean(a))
print("Standard Deviation :", np.std(a))

#=====================================================================
#=====================================================================

print("\n\nQ3. (Statistical Methods on 2D Array)")

# Creating 4x5 matrix
a = np.random.randint(20, 81, (4, 5))

print("Matrix:\n", a)

# Displaying statistics
print("\nMinimum :", np.min(a))
print("Maximum :", np.max(a))
print("Sum :", np.sum(a))
print("Mean :", np.mean(a))
print("Standard Deviation :", np.std(a))

# Row-wise sum
print("\nRow-wise Sum :", np.sum(a, axis=1))

# Column-wise sum
print("Column-wise Sum :", np.sum(a, axis=0))

#=====================================================================
#=====================================================================

print("\n\nQ4. (Reshape)")

# Creating array from 1 to 24
a = np.arange(1, 25)

print("Original Array:\n", a)

# Reshaping
b = a.reshape(4, 6)
c = a.reshape(3, 8)
d = a.reshape(2, 3, 4)

print("\n4 x 6 Matrix:\n", b)
print("Shape :", b.shape)

print("\n3 x 8 Matrix:\n", c)
print("Shape :", c.shape)

print("\n2 x 3 x 4 Array:\n", d)
print("Shape :", d.shape)

#=====================================================================
#=====================================================================
print("\n\nQ5. (NumPy Indexing - 1D & 2D)")

# Creating array
arr = np.array([[10,20,30,40],
                [50,60,70,80],
                [90,100,110,120]])

print("Array:\n", arr)

# Indexing
print("\nFirst Row:\n", arr[0])

print("\nLast Column:\n", arr[:,3])

print("\nCenter 2x2 Matrix:\n", arr[0:2,1:3])

print("\nEven Numbers:\n", arr[arr % 2 == 0])

#=====================================================================
#=====================================================================

print("\n\nQ6. (Advanced Indexing)")

# Creating matrix
a = np.random.randint(1,101,(5,5))

print("Original Matrix:\n", a)

# Diagonal
print("\nDiagonal Elements:\n", np.diag(a))

# Greater than 50
print("\nElements Greater Than 50:\n", a[a > 50])

# Replace values less than 30
a[a < 30] = 0

print("\nModified Matrix:\n", a)

#=====================================================================
#=====================================================================

print("\n\nQ7. (Arithmetic Operations)")

# Creating arrays
a = np.array([10,20,30,40])
b = np.array([1,2,3,4])

print("Addition :", a+b)
print("Subtraction :", a-b)
print("Multiplication :", a*b)
print("Division :", a/b)
print("Power :", a**b)
print("Modulo :", a%b)

#=====================================================================
#=====================================================================

print("\n\nQ8. (Matrix Multiplication)")

# Creating matrices
A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

B = np.array([[9,8,7],
              [6,5,4],
              [3,2,1]])

# Element-wise multiplication
print("Element-wise Multiplication:\n", A*B)

# Matrix multiplication
print("\nMatrix Multiplication:\n", A@B)

# * multiplies corresponding elements.
# @ performs actual matrix multiplication.

#=====================================================================
#=====================================================================
print("\n\nQ9. (Combined - Properties + Operations + Indexing)")

# Creating random matrix
a = np.random.randn(6,6)

print("Matrix:\n", a)

# Displaying properties
print("\nShape :", a.shape)
print("Size :", a.size)
print("Data Type :", a.dtype)

# Maximum and minimum index
print("\nMaximum Index :", np.unravel_index(np.argmax(a), a.shape))
print("Minimum Index :", np.unravel_index(np.argmin(a), a.shape))

# Extracting top-left matrix
print("\nTop Left 3x3 Matrix:\n", a[:3,:3])

# Replacing negative values with absolute values
a = np.abs(a)

print("\nModified Matrix:\n", a)

print("\nMean :", np.mean(a))

#=====================================================================
#=====================================================================

print("\n\nQ10. (Mini Project - Student Performance Analysis)")

# Creating marks of 10 students and 5 subjects
marks = np.random.randint(30,101,(10,5))

print("Student Marks:\n")
print(marks)

# Calculating total marks
total = np.sum(marks, axis=1)

# Calculating average marks
average = np.mean(marks, axis=1)

print("\nTotal Marks:")
print(total)

print("\nAverage Marks:")
print(average)

# Finding highest and lowest scorer
highest = np.argmax(total)
lowest = np.argmin(total)

print("\nHighest Scoring Student :", highest + 1)
print("Lowest Scoring Student :", lowest + 1)

# Overall class statistics
print("\nClass Mean :", np.mean(marks))
print("Class Standard Deviation :", np.std(marks))

# Sorting students according to total marks
index = np.argsort(total)[::-1]

print("\nTop 3 Students Marks:\n")
print(marks[index[:3]])

# Reshaping array into 5x10
new_marks = marks.reshape(5,10)

print("\nReshaped Array (5 x 10):\n")
print(new_marks)

#=====================================================================
#=====================================================================