#Project 1: Stone, Paper, Scissors Game:
'''stone =1 
   Paper = 0
   Scissors=-1
'''
computer = input("Enter computer's choice: ")
you = input("Enter your choice: ")
# guide = {"S":1,"P":0,"Sc":-1}
if (computer == you):
    print("it's drawn")
if(computer== "S" and you == "P"):
    print("you won")
elif(computer=="S"and you == "Sc"):
    print("computer won")
elif(computer == "P" and you == "S"):
    print("computer won")
elif(computer == "P" and you == "Sc"):
    print("you won")
elif(computer == "Sc" and you == "S"):
    print("you won")
elif(computer == "Sc" and you == "P"):
    print("computer won")