#Conditionals:
a = int(input("Enter your age: "))

#if else statement:

if (a>=18):
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")
print("\nend of if else statement")

# if elif else ladder:
if(0<a<=18):
    print("you can not fill the nominnes form for election")
elif(a<0):
    print("please enter the correct age")
elif(a==0):
    print("age input is invalid")
elif(a>=21):
    print("you can fill the nominnes form for election")
else:
    print("you have already known the result")
print("\nend of if elif else ladder")

# if statement can come alone but elif and else can not come alone.

# multiple if statements:

b=int(input("\nEnter the number of overs: "))
if(b>6):
    print("choose the batting")  # ---> This if statement is independent from the below if elif else ladder.
if(b>6):
    print("opening pair will be Parikshit and deep")
elif(2<b<6):
    print("choose the bumrah as bowler")
elif(b<2):
    print("choose the Parikshit as a bowler") # See, else statement is not compulsory in "if elif else ladder."
print("\nend of multiple if statements")