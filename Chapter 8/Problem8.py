#HW:1
def greatest_num(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
greatest_number = greatest_num(5,25,54)
print(greatest_number)

#HW:2
def cel_to_fahren(temp):
    return (9/5)*temp +32
print(f"{round(cel_to_fahren(232), 2)}") # "round" will "round off to the 2nd decimal point".

#HW:3
print("a ",end="")
print("b ",end="")
print() # due to this next printing will be on next line.

#HW:4
def sum_nat(n):
    if(n==1):
        return 1
    return n+sum_nat(n-1)
print(sum_nat(5))

#HW:5
def starpattern(n):
    for i in range(n):
        # print("*"*(n-i),end="")
        print("*"*(n-i))
        # print()
starpattern(int(input("Enter the number: ")))

#HW:6
def inch_to_cms(length):
    return length*2.54
inchtocms = inch_to_cms(12)
print(round(inchtocms,1))

#HW:7
list = ["Harry","Deep","Raj","rry", "Carry"]
print(list)
def wordremoval(list,name):
    n =[]
    for items in list:
        if(name.lower() == items.lower()):
            print(items)
            list.remove(items)
        else:
            n.append(items.strip(name)) # strip(name)--> it will remove the "chain of characters" given by 
            # argument "name" from the list elements in which it found.
    print(n)
wordremoval(list,"rry")
print(list)

#HW:8
def table(n,k):
    if(k==10):
        print(n*10)
        return n*10
    print(n*k)
    return table(n,k+1)
table(5,1)