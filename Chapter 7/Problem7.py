#HW:1
num = int(input("Enter the number: "))
# for i in range(1,11,1):
for i in range(1,11):
    print(i, " : ", num*(i))

#HW:2
l = ["Harry", "Soham","Sachin","Rahul"]
for items in l:
    if(items.startswith("S")):
        print("Hello,", items)

#HW:3
i=1
number = int(input("Enter the number: "))
while i<11:
    print(i*number)
    i+=1

#HW:4
N = int(input("Enter the number: "))
k =2
# flag = 1
while(k<N):
    if(not(N%k)):
        print("Not Prime number")
        # flag =0
        break
    k+=1
# if(flag):
else:
    print("Prime number")

#HW:5
n = int(input("Enter the number: "))
l=1
sum = 0
while l<=n:
    sum+=l
    l+=1
print(f"Sum of {n} natural numbers: ",sum)

#HW:6
z = int(input("Enter the number: "))
fact = 1
for i in range(1,z+1,1):
    fact *= i
print(f"factorial of the number {z} is: " , fact)

#HW:7
n = int(input("Enter the number for star pattern: "))
j = 0
k = 1
for i in range(n):
    while k<n:
        print(" ",end="")
        k+=1
    while(j<(i*2+1)):
        print("*",end="")
        j+=1
    j=0
    k=i+2
    print()

    #OR
n = int(input("Enter the number for star pattern: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(i*2-1),end="")
    print()

#HW:8
n = int(input("Enter the number for star pattern: "))
for i in range(n):
    while(j<i+1):
        print("*",end="")
        j+=1
    j=0
    print()

#HW:9
n = int(input("Enter the number for star pattern: "))
for i in range(n):
    if(i==0 or i==n-1):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print()

#HW:10
n = int(input("Enter the number for reverse table: "))
for i in range(10,0,-1):
    print(n*i)

