import random
n = random.randint(1,100)
a=-1
guesses = 0
while a!=n:
    guesses+=1
    a= int(input("Guess the number: "))
    if(a>n):
        print("Please guess the lower number")
    if(a<n):
        print("Please guess the higher number")
print(f"You have successfully guessed the number {n} in the number of guesses or attempts: {guesses}")
    