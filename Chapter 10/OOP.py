# OOP: Object Oriented Programming

class employee:
    # name --> we cannot generate only variable name solely,we have to assign value to it.Otherwise it throws error.
    name = "Pankaj"
    salary = 1200000  # All these are class attribute(trait or quality) : Attribute that belongs to the class rather
                      # than a particular object.
    lang = "py"

    def getinfo(self):
        print(f"The name of employee is {self.name}")
        print(f"The employee salary is: {self.salary}")
        print(f"The employee language is: {self.lang}")

    @staticmethod
    def greet():
        print("Hello, how are you?")
                             # the method whose name start with "__"(underscore(doubleunderscore may be)),
                             # is known as "Dunder method".
                             # This method is called "dunder method" which is automatically called.Note that
    def __init__(self,sal):  # not all "dunder methods" are called,but particularly this "__init__" is called.
        self.name = "Rohit"
        self.lang = "Java"
        self.salary = sal
        print("I am creating object")
 #   __init__() : constructor -->
 # __init__() is a special method which is first run as soon as the object is created.
 # __init__() method is also known as constructor.
 # It takes self-argument and also take further arguments. Note that we don't need to pass self to it while object
 # creation. Example --> harry = employee() is okay for def __init__(self): 

harry = employee(15000000) # "harry" is instance (object) of the class namely "employee"
# Instance Attribute: An attribute that belongs to the instance(object).
# harry.name = "Raj" # This is instance(object) attribute(trait or quality) which has priority over class attribute.
# whenever we want to "assign the value" or "getting(retrieval) the value" of (harry.attribute) obj.attribute :
# we check for : 1) Is attributes present in object? --> if this is not found then, it check for: 
#                2) Is attributes present in class?    
harry.getinfo()
harry.name = "Deep" # --> It will overwrite the class attribute "name".

harry.getinfo() # --> This means that employee.getinfo(harry), thus it passes harry(object) as an argument
#.If function did not have argument then it will throw error,hence we either compulsory keep methods(functions)
# with one argument mostly named as "self"(good practice) or we write "@staticmethod" before declaring the function.

harry.greet()