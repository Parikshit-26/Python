#HW:1
class Programmer:
#     name = "Harry"
#     language = "py" # No need of these declarations when you use constructor __init__
#     skills = "ml"
#     salary = 120000000
    def __init__(self, name , salary, language,skills):
        self.name = name
        self.language = language
        self.salary = salary
        self.skills = skills

    def getinfo(self):
        print("Hello, this is for getting info")
        print(f"salary {self.salary}, {self.language}, {self.skills}, {self.name} ")
obj = Programmer("Harry", 1999999999, "Java", "CSS")
obj.getinfo()
print(obj.skills)

#HW:2&4
class calculator:
    def __init__(self, variable):
        self.variable = variable
    def square(self):
        return self.variable**2
    def cube(self):
        return self.variable**3
    def sqrt(self):
        return self.variable**(1/2)
    
    @staticmethod
    def greet():
        print("Hello, I am a good boy")
cal = calculator(1296)
list = [cal.sqrt(), cal.square(),cal.cube()]
print(list)
cal.greet()

#HW:3
class sample:
    a = "willitchange"
    def getinfo(self):
        print(f"class attribute a when called as instance attribute will change to: {self.a}")
obj = sample()
obj.a = "Yesitwillchange"
obj.getinfo()

#HW:5
class Train:
    def __init__(self, p, tc):
        self.price = p
        self.travelclass = tc
    def getstatus(self):
        print("Status is under pending")
    def bookticket(self):
        print("1000 rupees for one seat")
obj = Train(500,"firstclass")
obj.bookticket()
obj.getstatus()

#HW:6
class practice:
    name = "Deep"
    def getinfo(har): # we can use anything instead of "self",but it considered as bad practice.
        print("The name: ",har.name)
p = practice()
p.getinfo()
