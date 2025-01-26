#HW:1
Dic = {"padhana":"Study","likhana":"Write","Daudana":"Run","Chalana":"Walk"}
word = input("Enter the word you want meaning of: ")
print(Dic[word])
print(Dic)

#HW:2
s1 = set()
for i in range(0,8):
    s1.add(int(input("Enter the numbers: ")))
    # s1= (int(input("Enter the numbers: ")))

print(s1)

#HW:3
s2 = {18,"18"}
print(s2)

#HW:4
s= set()
s.add(20)
s.add(20.0) # In python 20(int) and 20.0(floating point) are the same ,even their data type is different
# but they are numerically same , so python considers them as same.
s.add('20')
print(len(s))

#HW:5
s3={}
print(type(s3))

#HW:6
my_dic = {}
list = ["Parikshit", "Raj", "Deep","Madhavi"]
for i in range(0,4):
    my_dic.update({list[i]: input("Enter your favourite language: ")})
print(my_dic.items())

#HW:7
'''Question --> If the names of two friends are same, what will happen to the program in HW:6?
   Answer --> It will update the same key and erase the previously assigned value viz.language'''
my_dic_1={}
list_2 = ["Parikshit","Raj","Deep","Parikshit"]
for i in range(0,4):
    my_dic_1.update({list_2[i]: input("Enter your favourite language: ")})
print(my_dic_1.items())

#HW:8
'''Question --> If language of two friends are same, what will happen to the program in HW:6?
   Answer --> It doesnot matter.'''
my_dict_2={}
for i in range(0,4):
    my_dict_2.update({list[i]:input("Enter your favourite language: ")})
print(my_dict_2.items())

#HW:9
# s_4 = {8,7,12,"Harry",[1,2]} # --> We cannot add the list in the set.So it will throw error.
'''You cannot even have a list as an element in a set because sets are in python require all their elements to 
be immutable and hashable. Lists are mutable and not hashable, so they cannot be added to a set.'''

