'''In c++ when we invoked the variables in the same class where
they are declared, we don't need to use "obj.variablename" .i.e. impicit call is used.
No need of instances.
But, In Python , we have to use "self.variablename"  even in the same class,bcz python prefers
explicit call.

Also In c++ : If both base and derived classes have constructors, base class constructor is
   executed first.
   But, In python everyone's individual constructors will executed.'''

# In python , everything is class. tuples , list , int, str, etc. all are classes.


#Inheritence:
class employee:
    name = "Default name"
    salary = "56k"

    def __init__(self, lang):
        self.lang = lang
        print("constructor of Parent class-employee")
    def getinfo(self):
        print("This is topic for inheritence")

class programmer(employee):
    def __init__(self, lang):
        self.lang = lang
        print("constructor of child class-programmer")

a = employee("c++")
b = programmer("Java")
a.getinfo()
b.getinfo() # this is object of child class but accessing the method of parent class.

# Multiple Inheritence: In this Inheritence child class is derived from multiple parent classes.
class emp:
    name = "Default name"
    salary = "56k"

    def __init__(self, lang):
        self.lang = lang
        print("constructor of Parent class-employee")
    def getinfo(self):
        print("This is topic for Multiple-inheritence")

class coder:
    def __init__(self, city):
        self.city = city
        print("constructor of Parent class-coder")


class programmers(emp,coder):
    def __init__(self, lang):
        self.lang = lang
        print("constructor of child class-programmer")

c= emp("Javascript")
d= programmers("julia")
# e=coder() # when I dont pass required number of arguments,when creating object,
#it will throw error.
f = coder("bgl")
c.getinfo()
d.getinfo()
# e.getinfo() --> this will throw error, bcz, getinfo() method is not defined in class coder 
# and it is a parent class.

#Multilevel Inheritence:  grandfather-> father->child (structure like :ancestors are considered)
class state:
    a=1
    def __init__(self,name,pop):
        self.name = name
        self.pop = pop
        print("this is  grandfather-constructor")
    def getinfo(self):
        print(f"name - {self.name}, population - {self.pop}")

class district(state):
    b=2
    def __init__(self, name,pop):
        self.name = name
        self.pop  = pop
        print("This is father-constructor")

class city(district):
    c=3
    def __init__(self, name,pop):
        self.name = name
        self.pop  = pop
        print("This is child-constructor")
first = state("MH", 120)
second = district("JL",60)
third = city("AN",30)
first.getinfo()
second.getinfo()
third.getinfo()
o = state("K",130)
print(o.a)
# print(o.b)# --> it will throw error.as there is no attribute in Employee class

o = district("CD",65)
print(o.a,o.b)

o = city("C",32)
print(o.a,o.b,o.c)

#super() method : It calls the constructor of class and its all ancestors(parent classes) 
#super() method is used to access the methods of a super(parent) class in the derived class 
class I:
    def __init__(self):
        super().__init__() #--> this will not throw error, even it has no ancestor,so it will
        # call only self constructor(I)
        print("constructor of I")
class F(I):
    def __init__(self):
        super().__init__() # --> call constructors of self(F) and I in order of I->F
        print("constructor of F")
class G(F):
    def __init__(self):
        super().__init__() # --> call constructors of self(G) and F and I in order of I->F->G
        print("constructor of G")
k = I()
L = F()
M = G()
#super method() fails when you pass multiple arguments (other than "self") to constructor.



'IMPORTANT:'
#Class method: A class method is a method which is bound to the class and not to the object of class. 
# whatever start with "@" is called as decorator.
class E:
    a=1
    @classmethod # with classmethod, we use "cls" instead of "self". This prioritize the class
    # attribute over the instance attribute. 
    def show(cls):
        print(f"the class attribute a is {cls.a}")
    
    @property # this is also called "getter method", it is related to "abstraction and encapsulation"
    # As we know name() is method here, but we get it as variable(attribute) while calling
    # that is we do not use "()" , we use only "p.name"(similar to accessing the variable by object)
    #@property decorator makes this possible to create "kname" attribute(variable) inside the name() method
    # but access as "name" attribute(variable).
    def name(self):
        # return f"{self.fname} {self.lname}"
        return self.kname
    
    @name.setter #this is called "setter method" which further assigns some arguments to the
    # previously made attribute by @property (getter method).here we assign "value" argument
    # to the attribute(variable) "kname" 
    def name(self,value):
        self.kname=value
        # self.fname= value.split(" ")[0]
        # self.lname= value.split(" ")[1]

    @property
    def find(self):
        return self.onlyforname
    
    @find.setter
    def find(self, answer):
        self.onlyforname = answer
p = E()
p.a=45 # instance attribute "a" which is set as a=45
p.name = "Parikshit Mahajan" # see access "name()" method  as attribute(variable) 
print(p.kname) # see, printed internally developed attribute
# print(p.name) # see, printed method (name()) which is looking as attribute to user.
# print(p.fname, p.lname)
p.show() # as we use @classmethod decorator, it will give us the value of class attribute (a=1)
t = E()
t.find = "No for any method identity"
print(t.find)
# print(t.onlyforname)




# Operator overloading:
'''1) Operator in python can be overloaded using dunder methods.
   2) These methods are called when a given operator is used on the "objects"(instances).
   3) Operators in python can be overloaded using the following methods:
    p1+p2  p1.__add__(p2)
    p1-p2  p1.__sub__(p2)
    p1*p2  p1.__mul__(p2)
    p1//p2  p1.__floordiv__(p2)
    p1/p2  p1.__truediv__(p2)
    4) other dunder/magic methods in python:
    __str__() used to set what gets displayed upon calling str(obj) (after conversion of object to string)
    __len__() used to get what gets displayed upon calling __len__() or len(obj)
        '''
class number:
    def __init__(self, n):
        self.n = n
    def __add__(self, num): # here self and num are used to represent the objects
        return self.n + num.n # both objects' attribute "n" is added here using operator overloading

n = number(1) # obj 1
m = number(2) # obj 2
print(n+m) # see here we called dunder method __add__ to add the objects attribute "n".
#above is function overloading for operator "+"
