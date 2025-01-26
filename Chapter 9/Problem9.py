#HW:1
with open("poems.txt") as p:
    name = p.read()
    print(name.find("twinkle")) # It will return the index of "t" in "twinkle"
    print("Twinkle".lower() in name) #It will return bool variable(true or false)
    print("twinkle" in name)         #It will return bool variable(true or false)

#HW:2
def game():
    Score = int(input("Enter your score: "))
    return Score
Score = game()
with open("Hi_score.txt") as h:
    Hi_Score = h.read()
    # print(Hi_Score)
if(int(Hi_Score)<Score):
        with open("Hi_score.txt","w") as k:
             k.write(str(Score))

#HW:3
for i in range(13,19):
     with open(f"table_{i}.txt","w") as t:
        for k in range(1,11):
            table = f"{k*i}\n"
            t.write((table))

#HW:4
str =""
with open("Donkey.txt","r") as d:
     str = d.read()
     print(str)
     str = str.replace("donkey","#####")
with open("Donkey.txt","w") as k:
    k.write(str)

#HW:5
list = ["donkey","ox","stupid","nonsense","insane"]
str =""
with open("Censored.txt") as c:
    str = c.read()
    print(str)
    for i in list:
        str = str.replace(i,"#####")
with open("Censored.txt","w") as c:
    c.write(str)

#HW:6&7
with open("log_file.txt") as l:
    def find(python):
        k=1
        lines = l.readline() # Note that next readline() function call automatically read the next line.
        while(lines != ""):
            if(python in lines):
                print("line number is: ",k)
                k+=1
                print("found")
                print(lines,end="")
                lines = l.readline()
            else:
                k+=1
                print("not found")
                print(lines,end="")
                lines= l.readline()
    find("python")
'''The reason for the blank lines appearing in the terminal
when you don’t use end="" in the print() function is due to
the newline character (\n) at the end of each line in the file. That means
When reading from a file, the "\n" at the end of each line is part of the string returned by readline().'''

#HW:8
with open ("this.txt") as source , open("that.txt","w") as destination:
    destination.write(source.read())

#HW:9
def findduplicate():
    with open("this.txt") as s, open("that.txt") as d:
        read1=s.read()
        read2=d.read()
    if (read1 == read2): # See if statement is out of the scope of "with" statement;still read1 and read2 are accessible.
        #Bcz, they are local variables of function "findduplicate()". But, note that files would not be accessible 
        #after the closing of "with" statement.
        print("\nYes, Both files are identical.")
    else:
        print("\nNo, Both files are not identical.")
findduplicate()

#HW:10
with open("wipeout.txt","w") as w:
    # w.write("")
    # w.truncate(0) # this will truncate the file to zero length of string
    pass # This will open the file and wipe it out and immediately close it

#HW:11
import os 
os.rename("name.txt","renamed_by_python.txt") # Rename of the file can only happen through importing module("os")
#We don't need to open the file for renaming it.