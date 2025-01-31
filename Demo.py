print("hello python guys")
def add(a, b):
    return a + b

a = 3
result = add(a, 5)
print(result)  # Output: 8

for i in range(3):
    print(i)

print("Hello world")

a = [[1,2,3], 
     [4,5,6],
     [7,8,9]]
print(a)

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))
# create a list of size m*n
A= []
for i in range(0,m*n):
    A.append(int(input("Enter the entry: ")))
print("Now enter the entry of vector b")    
b = []
for j in range(0,n):
    b.append(int(input("Enter the entry: ")))

p = len(b)
print(p)
# print(len(A))
# l = len(A)/p
# print(l)
Ab = []
for k in range(0,m*n,p):
    ele = 0
    for i in range(0,p):
        ele += (A[k+i]*b[i])
    Ab.append(ele)


print(Ab)

