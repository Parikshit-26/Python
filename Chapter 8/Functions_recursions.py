#Functions:
def greet():
    print("Hello World")
    return
print(greet()) # It will print "None", as function did not return anything.
def avg():
    num_1 = int(input("Enter the number: "))
    num_2 = int(input("Enter the number: "))
    num_3 = int(input("Enter the number: "))
    average = (num_1+num_2+num_3)/3
    return average

print(avg())

# functions with arguments:
def forwarddiff(f,x,h):
    der = (f(x+h)-f(x))/h
    return der
def centraldiff(f,x,h):
    der = (f(x+h)-f(x-h))/(2*h)
    return der

def f(domain_value): #---> See I have declared function f below and passed it as an argument earlier without declaring 
    #function prototype(as in c++).  No need of function prototype in python.
    return domain_value**2

print(forwarddiff(f,2,10**(-5)))
der_bycentdiff = (centraldiff(f,2,10**(-5)))
print(der_bycentdiff)

def g(name,ending = "Thank you"):
    print(f"Good morning, {name}, {ending}")

g("Harry", "Thanks")
a = g("Deep") #--> It will take default argument for variable (string type) "ending" viz. "Thank you". 
# If we do not pass argument for ending and also there is no default argument for "ending", then it will throw error. 
print(a) # As function didnot return anything it will print "None".

#Recursion:
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

factorial = fact(int(input("Enter the number: ")))
print(factorial)