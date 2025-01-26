a = "Raj"
b = 'Deep'
c = '''Kirloskar'''
print(a,b,c)

name = "aqbcdefght"
nameshort = name[8:] # whole "name" string is printed
print(nameshort)
print(name[1:4])  # It includes character at starting index 1 but not the character at ending index 4
print(name[:10])
print(name[:])
print(name[1:7:4]) # First it will consider string "qbcdef" and then it prints finally string "qbcde - bcd = qe"              # starting index(q) to the second-last index character (c))
print(name[2:9:5])                         

#String Functions

print(len(name))
print(name.count("c"))
print(name.endswith("wer"))
print(name.capitalize())
print(name.startswith("aq"))
print(nameshort.upper())
nameshort = "HT QW"
nameshort = nameshort.replace("HT", "jh") # You have to assign this "replace()" function to some string then it will work, 
print(nameshort)           # Direct print will not work for "replace()" function.Bcz, Strings are immutable, that means
print(nameshort.find("j")) # replace() function didnot change the original string, it creates the new string
                           #  and original one remains intact.

# Escape Sequence Characters
print("Raj is a good boy\nbut not the bad boy") # \n : goes to next line
print("Raj is very \"very\" good boy")
print('Deep is very \'very\' good boy')   #  \'  \' : use for taking words or phrases in single inverted commas
                                         #  \"  \" : use for taking words or phrases in double inverted commas
                                         # \t : tab ; \ \ : Backslash