#File I/O: 
'''open() function takes two parameters --> 1) file name, 2)mode of opening 
There are four types of "mode of opening :
I)  "r" (Read mode) :
Opens a file for reading. If the file does not exist, it raises a "FileNotFoundError".

II) "w" (Write mode) :
Opens a file for writing. If the file exists, it truncates (overwrites) the file. If the file does not exist, it creates a new one.

III) "a" (Append mode) :
Opens a file for appending. Data is added to the end of the file without truncating it. If the file does not exist, it creates a new one.

IV) "x" (Exclusive creation mode)
Creates a new file. If the file already exists, it raises a "FileExistsError".

By default mode of opening parameter is "r" (Read mode), when you give only first parameter as an argument to open() function.'''

# open() function with "w" (Write mode):

file = open("file_1.txt","w") # I have not created text file namely "file_1.txt",but passed it as first argument 
#with "w" as second argument.Due to "w", this file was created in same folder where this ".py" file located. 
text = """I am good,
what's about you? 
Could you please schedule the zoom meeting as soon as possible?"""
file.write(text)
file.close() # This is optional , but it's a good practice to close the file when your work with that file has done.

f = open("file_1.txt","w") # It will overwrite the "file_1.txt" file.
overwrite = "Erase all" 
f.write(overwrite)
f.close()

# open() function with "r" (Read mode) (Default mode):
reply = open("file_2.txt")
data = reply.read()
print(data)
reply.close()

k = open("file_1.txt")
lines = k.readlines() # to read the all lines written in file. Basically another option for read() function.
print(lines, type(lines)) # type(lines) will be a "list".
k.close()

#open() function with "a" (Append mode):
r = open("file_1.txt", "a")
re = "\nYes, this time is suitable for me."
r.write(re)
r.close()


#open() function with "x" (Exclusive creation mode):
p = open("file_3.txt","x") # When we run this code second time, it will throw error, bcz this "x" mode is 
# for creating new file, if that file exists then it will throw error
add = "I want to join you,guys"
p.write(add)
p.close()

#with statement : When we get out of "with" statement, it automatically close the already open file. that is 
                 # no need of close() function
with open("file_3.txt") as l:
    print(l.read())
  
                    