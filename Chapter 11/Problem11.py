#HW:1
class Two_D:
    def set(self, i , j):
        self.x = i
        self.y = j
    def get(self):
        print(f"vector-x coordinate {self.x} , vector-y coordinate {self.y}")
    
class three_D(Two_D):
    def set_third(self, i , j ,k):
        self.z = k
        self.set(i ,j)
    def get_third(self):
        self.get()
        print(f"3-D vector-z coordinate {self.z}")

vector_1 = Two_D()
vector_2 = three_D()
vector_1.set(5,4)
vector_2.set_third(4,8,16)
vector_1.get()
vector_2.get_third()

#HW:2
class animal:
    # type = "domestic"  # No need we can define these attributes directly in method,too
    def type(self, type):
        self.type = type
    def getinfo(self):
        print(f"type of animal: {self.type}")
class pets(animal): 
    # animal_name = "tommy" # No need we can define these attributes directly in method,too
    def name(self, animal_name):
        self.name = animal_name
        print(f"animal_name: {animal_name}")
class dog(pets):
    # barking = "wild"  # No need we can define these attributes directly in method,too
    def __init__(self,colour):
        self.hair=colour
        print(f"hair colour: {self.hair}")
    def bark(self,barking):
        self.barking = barking
        print(f"barking of muffy: {self.barking}")
muffy = dog("lightorange")
muffy.bark("cute")
muffy.name("muffy")
muffy.type("member_of_family")
muffy.getinfo()

#HW:3
class employee:
    def __init__(self):
        self.salary = 300
        self.increment = 10
        print(f"constructor of class, salary: {self.salary}, increment: {self.increment}")
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, inc):
        self.increment = ((inc/self.salary)-1)*100
    
hari = employee()
hari.salaryAfterIncrement = 600
# print(hari.salaryAfterIncrement)
print(hari.increment)
#HW:4
class complex:
    def __init__(self , x, y):
        self.r = x
        self.i = y
    def __add__(self,c2):
        return complex(self.r + c2.r , self.i + c2.i)
    def __mul__(self,c2):
        real_part = self.r * c2.r - self.i*c2.i
        imag_part = self.r * c2.i + self.i *c2.r
        return complex(real_part,imag_part)
    def __str__(self):
        return f"{self.r} + {self.i}i" # this str function overloading of "string" 
    # is used by every object of class , whether that object has called this __str__()
    # dunder method or not, it does not matter.
com_1 = complex(1,2)
com_2 = complex(2,3)
print(com_1+com_2,type(com_1+com_2))
print(com_1*com_2)
print(str(com_1))


#HW:5,6 & 7
class vector:
    def __init__(self,l):
        self.x,self.y,self.z =l
    def __add__(self,other):
        result = vector([self.x +other.x,self.y+other.y,self.z+other.z])
        return result
    def __mul__(self,other):
        result = self.x *other.x + self.y*other.y + self.z*other.z
        return result
    def __str__(self):
        return f"vector({self.x}i + {self.y}j + {self.z}k)"
    def __len__(self):
        return 3
        
    
v1 = vector([1,2,3])
print(len(v1))
v2 = vector([3,4,5])
v = v1+v2
print(v)
# print(v1+v2)
print(v1*v2)
print(str(v2))
