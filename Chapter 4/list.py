#list
friends = ["Akash", "orange",False, 7, 56.45] # Python lists are containers that 
                                               # can store a set of values of any data type.
print(friends[0], friends[3], friends[2])     

name = "apple"
print(name[0], name[3]) 
# name[3]=q # This will throw error, bcz Strings are immutable.
friends[0]="grapes" # This is valid, bcz lists are mutable.
friends[1]=32  # We can change data type of elements of already created list.
print(friends[0], friends[1])                                      
print(friends[0:3])


# list_Methods()
print(friends)
friends.append("Harry")
print(friends)
l1 = [2,34,21,45,32,51,1,11]
l1.sort() # arrange l1 in ascending order
print(l1)
# print(l1.sort()) -> It will return "None"
# print(l1.reverse()) -> It will return "None"
l1.reverse() # Note original list l1 will change, always.
print(l1)
l1.insert(3,17)  # It insert integer 17 at index 3 in list l1.
print(l1)
l1.pop(2) # It will delete element at index 2 and return its value.
print(l1.pop(1)) # -> It will return the value of element at index 1 in list l1.
print(l1)
# l1.remove(12) It will throw error, as 12 is not in list l1.
l1.remove(21) # It will remove 21 from list l1.
print(l1)

#Tuples
a = (1,2,34,45.43,"Rohan") # Tuples are immutable. it is similar to list, the difference between them is list is
 # mutable but tuples are immutable
print(type(a))
b =(1) # type(a) = int
print(type(b))
c = (1,) # type(a) = tuple
print(a)
print(c)
print(type(c))

# Tuples_Methods
print(a.count(45)) # return the frequency of element "45" present in tuple "a"  
print(len(a)) # return length of tuple "a"
print(34 in a) # Return true if 34 is present in tuple "a" otherwise return false
print(a.index(2)) # return index of element "2" in tuple "a"


