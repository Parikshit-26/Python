#Dictionary

marks = {"Parikshit":65,"Raj":75,
"Deep":95, 0:"Shia", "Parikshit":45, "Sudama":[12,23,45]} # Here Parikshit is overwrite by new value 45.
# We can store list also in dictionary As key-value pair where key must be name of list.
print(marks, type(marks))
# print(marks[0]) ---> It will throw error, As Dictionary is:
'''1)list of key and value , you have to search using key;where key = LHS & value = RHS
   2)dictionary is mutable, unordered and indexed (#function will be in backend s.t. it will find any key
    in time complexity of O(1))
   3)we can not add duplicate keys '''
print(marks["Deep"])
Exam_marks = [['Raj',67], ["Sudama",67]] # This is list of list.
print(Exam_marks, type(Exam_marks))
# print(Exam_marks["Sudama"]) ---> This will throw error,bcz we can't search in list using elements of list.
print(Exam_marks[1])


#Dictionary_methods
print(len(marks))
print(marks.items()) # it will print dictionary in tuples format.
print(marks.keys())
print(marks.values())
marks.pop("Raj")
print(marks)
print(marks.get("Pari")) # As key is not present, it will print "None".
# print(marks["Pari"]) # --->As key is not present, it will "throw error".
marks.update({"Parikshit":100, "Renuka":99})
print(marks)
Grade = marks.copy()
print(Grade, type(Grade))
list = [1,2,3,4,5]
my_dict = dict.fromkeys(list,0)
print(my_dict) # we have created dictionary with all keys having 0 value from list. 

#Set : Set is a collection of well defined and non-repititive objects(elements)
d = {} # This will give you empty dictionary.
s = set() # this will create empty set. 
set = {1,2,3,4,5, 'Harry'} # Note that set and dictionary both are written in curly brackets. But sets are:
'''1) unordered -> Elements order doesn't matter.
   2) unindexed -> Cannot access elements by index.
   3) there is no way to change items in sets. Of course sets are mutable .i.e. you can add or remove
      the elements(items); but you can not replace the existing item by other item (in one go), you 
      have to remove the existing item first and then add new one (2 step process). Actually It does not
      make any sense to change the existing item, as set is for well defined objects. If you want to change 
      the existing items in such cases , use other type of data structures.
   4) Sets cannot contain duplicate values. '''
print(set, type(set))
set.add(45)
set.remove(5)
print(set)
print(len(set), len(s))
s_1 = {1,2,3,45,56,6,76,76,7} # To print the duplicate elements use list, as set will not print duplicate elements. 
l_1 = [1,2,3,45,56,6,76,76,7] 
print(s_1, l_1)

#Set_methods
s1 = {1,3,45,67}
s2 = {45,2,67,99}
print(s1.union(s2))
print(s1.intersection(s2))
s1.pop() # remove arbitrary element from set.
print(s1) 
print(s1-s2,s2-s1) # let say s1-s2 has no element then it will print "set()"

