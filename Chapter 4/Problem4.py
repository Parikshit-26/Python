#HW:1

fruits = [] # We have created the empty list namely "fruits".In python list is dynamic.

for i in range(0,7): # It will not include 7
  # fruits[i] = input("Enter the Fruit Name: ") ---> error is :
# You are trying to assign a value to fruits[i] before the list fruits has any elements at the specified index i.
# Lists in Python are dynamic, so you can append elements but cannot assign to an index that does not already exist.
  fruit = input("Enter the Fruit Name: ") # Uncomment this
  fruits.append(fruit)  # Uncomment this

print("Fruits list", fruits) # Here printed fruits list elements will be written in '' (single inverted commas).
  #As they are strings.

#HW:2
StudentMarks = []
for k in range(0,6):
  #mark = int(input("Enter the Marks of", k,"th Student: ")) # --> This will throw error, Bcz you are passing 
  #more than one argument to input() function (k and input by user that you want). You can use such syntax with
  # print() function but not with input(). To use with input() function use {f"string}
  mark = int(input(f"Enter the mark of {k+1}th student: "))
  StudentMarks.append(mark)
StudentMarks.sort()
print("StudentMarks list: ", StudentMarks)# Here printed StudentMarks list elements won't be written in ''
  # (single inverted commas).As they are integers and not the strings.

#HW:3
a = (34,43,"rohan", "Santosh",45.67)
print(type(a))
print(a[2])
#a[2]= 67 # It throws error, Bcz tuple is immutable.
print(a[2])

#HW:4
num=[2,3,1,12]
print(sum(num)) # Inbuilt sum() function to sum the elements of list.
sum =0
for i in range(0,4):
 sum += num[i]
print("Four Numbers sum: ",sum)

#HW:5
t =(1,0,12,0,0.0,0.23,23)
print(t.count(0)) # It will count 0.0 also.