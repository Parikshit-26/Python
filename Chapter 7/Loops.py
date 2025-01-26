#Loops:

#while loop:
i =1
# while(i<3):
while i<3:
    print(i**2)
    i +=1 # --> += is the valid operator in which always write firstly the operation that you want to perform. 

# for loops:

for i in range(0,3): # range(start ,stop, step-size)
    print(i**3)
# for i in range(3): # range(start ,stop, step-size)
#     print(i**3)
# for i in range(0,15,3): # range(start ,stop, step-size)
#     print(i**3)

list = [2,34,45,32]
for i in list:
    print(i)

# for loop with else statement(optional):
for items in list:
    print(items)
else:
    print("This else statement with for loop is optional and it runs after the \"for loop\" exhausted")
'''This else statement with for loop is optional and it runs after the "for loop" exhausted.But if we use
"break" statement in the "for loop", then "else" statement will not execute.'''
# Pass statement : "Do Nothing"
for i in range(2):
    pass     # --> It is used to avoid the error,bcz sometimes we want to complete already written "for loop"
        # later on. so indentation error will occur if we left the for loop without its completion.
    # print("Hello") # --> It will print "Hello" two times.
print("for loop has not done anything")

#continue statement : "skip this iteration"
for i in range(3):
    if(i==1):
        continue
    print(i+2)

#break statement : "break the loop right now"
for i in range(4):
    if(i==1):
        break
    print(i-2)
