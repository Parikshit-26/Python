import numpy as np
# import numpy as np
# print(np.__version__)   

np.random.seed(42)  # if you do not use the seed, 
#you will get different random numbers each time you run the code and 42 is just a random number
# you can use any number you want. number "42" has some special meaning in the universe of computer science
# that is why people used it mostly.
data = np.random.rand(3,3) # make a 3x3 matrix with random numbers taken from a uniform (continuous) distribution between 0 and 1
# data = np.random.randn(10) # make a 1D array with 1000 random numbers taken from a normal (Gaussian) distribution with mean 0 and standard deviation 1
print(data)
print(type(data))
print(data.shape)


# mat_1 = np.linspace(0,10,4)
mat_1 = np.arange(0,10,2) # 1D array
print("mat_1: " ,mat_1)

mat_2 = np.full((3,3),1) # 2D array
# print("mat_2: ", mat_2)
print(np.sum(mat_2)) # return only the single value of all elements
print(np.cumsum(mat_2)) # return 1D array with number of entries = number of total entries in mat_2 matrix

A = np.full((3,3),2)
B = np.full((3,3),4)
C = np.matmul(A,B)
D = np.multiply(A,B)
E = np.dot(A,B)
F = np.divide(A,B)
print(A , B)
print(f"matrix multiplication: {C}")
print(f"element wise multiplication: {D}")
print(f"dot product of two matrices: {E}")
print(f"element wise division: {F}")

'''1. Creating Arrays
np.array([1, 2, 3]) → Create an array
np.zeros((3,3)) → Create a 3×3 matrix of zeros
np.ones((2,2)) → Create a 2×2 matrix of ones
np.full((2,2), 7) → Create a 2×2 matrix filled with 7
np.eye(3) → Create a 3×3 identity matrix
np.linspace(0, 10, 5) → Create 5 equally spaced numbers from 0 to 10
np.arange(0, 10, 2) → Create an array [0, 2, 4, 6, 8]

2. Random Number Generation
np.random.rand(3,3) → Random numbers from uniform distribution (0 to 1)
np.random.randn(3,3) → Random numbers from normal distribution (mean 0, std 1)
np.random.randint(1, 10, (2,2)) → Random integers between 1 and 10 in a 2×2 matrix
np.random.seed(42) → Set seed for reproducibility
np.random.normal(loc,scale,size) → Normal distribution with mean = loc, 
                                    std deviation = scale , size = shape  of the output array

3. Array Operations
np.sum(arr) → Sum of all elements
np.mean(arr) → Mean of array
np.median(arr) → Median of array
np.std(arr) → Standard deviation
np.var(arr) → Variance
np.min(arr) / np.max(arr) → Minimum & maximum values
np.argmin(arr) / np.argmax(arr) → Indices of min & max values
np.cumsum(arr) → Cumulative sum of elements
np.cumprod(arr) → Cumulative product

4. Indexing & Slicing
arr[1] → Access 2nd element
arr[1:4] → Slice from index 1 to 3
arr[:3] → First 3 elements
arr[-1] → Last element
arr[::2] → Every second element
arr.reshape(3,2) → Reshape to 3×2 matrix

5. Linear Algebra (NumPy.linalg)
np.dot(A, B) → Dot product of two matrices
np.matmul(A, B) → Matrix multiplication
np.linalg.inv(A) → Inverse of a matrix
np.linalg.det(A) → Determinant of a matrix
np.linalg.eig(A) → Eigenvalues & eigenvectors
np.linalg.solve(A, b) → Solve a system of linear equations

6. Element-wise Operations
np.add(A, B) → Element-wise addition
np.subtract(A, B) → Element-wise subtraction
np.multiply(A, B) → Element-wise multiplication
np.divide(A, B) → Element-wise division
np.exp(A) → Exponential of each element
np.log(A) → Natural log of each element
np.sqrt(A) → Square root of each element

7. Sorting & Searching
np.sort(arr) → Sort an array
np.argsort(arr) → Get indices of sorted elements
np.where(arr > 5) → Get indices where condition is met
np.unique(arr) → Get unique elements

8. Boolean Masking
arr[arr > 5] → Get elements greater than 5
np.any(arr > 5) → Check if any element > 5
np.all(arr > 5) → Check if all elements > 5'''
