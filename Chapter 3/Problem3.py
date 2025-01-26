# HW:1
#print(input(),"Good afternoon")
name = "Deep"
print("Good afternoon", name)
print("Good afternoon " + name + "") # Concatenation of Strings
print(f"Good afternoon, {name}") # this is called "f-string", which avoids the concatenation of strings(string variables).

#HW:2
# name = input("Your Name")
# date = input("add the date")
# print(f'''Dear {name}
#        You are selected!
#       {date}''')

letter = '''
       Dear <|Name|>
          You are selected!
          <|Date|>'''
print(letter.replace("<|Name|>", "Raj").replace("<|Date|>","05-01-25"))

#HW:3
Sent = "Raj is a good  boy"
print(Sent.find("  "))

#HW:4
Sent = "Deep is a good  boy" #Here, We are defining variable "Sent" newly .i.e. assigning new string to the same variable "Sent".
print(Sent.replace("  "," "))
"""Strings are immutable which means that you cannot change them by running functions on them. But lists are not immutable."""
#HW:5 
letter = "Dear Harry, this python course is nice. Thanks!"
print(letter)
letter = "Dear Harry,\n\tThis python course is nice.\nThanks!"
print(letter)



