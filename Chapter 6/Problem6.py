#HW:1
num= []
Int_max = -10**18
for i in range(0,4):
    num.append(int(input("Enter the number: ")))
    if(num[i]>=Int_max):
        Int_max = num[i]
    else:
        continue

print("Greatest number is: ",Int_max)

#HW:2
subjects = ["Hindi", "Marathi","Math"]
Marks = {}
sum_marks = 0
flag = 1
for i in range(0,3):
    Marks.update({subjects[i]: int(input("Enter the marks: "))})
    sum_marks += Marks.get(subjects[i])
    if(Marks.get(subjects[i])>33):
        print(f"Student successfully passed in the {subjects[i]}")
    else:
        print(f"Student unsuccessfully failed in the {subjects[i]}")
        flag =0
percent = sum_marks/3
if(percent>40 and flag):
    print("student is passed",percent)
else:
    print("student is failed",percent)

#HW:3
comment = ["make a lot of money", "buy now", "subscribe this", "click this"]
phrase = input("Enter the phrase: ")
flag = 1
for i in range(0,4):
    if(comment[i] in phrase):
        print("spam detected")
        flag = 0 
if(flag):
    print("spam did not detect")

#HW:4
username = input("Enter the username: ")
if(len(username)<10):
    print("Number of characters is less than 10")
else:
    print("Number of characters is grater than or equal to 10")

#HW:5
list = ["Rahul", "Deepak","Deep", "Raj", "Mehul", "Sandeep"]
name = input("Enter the name: ")
# flag = 1
# for items in list:
#     if(items == name):
#         print("Selected")
#         flag = 0
#         break
# if(flag):
#     print("Not selected")
if name in list:
    print("Selected")
else:
    print("Not selected")

#HW:6
marks = int(input("Enter the marks: "))
grade = "error"
if(100>=marks>90):
    grade = "Ex"
elif(90>=marks>80):
    grade = "A"
elif(80>=marks>70):
    grade = "B"
elif(70>=marks>60):
    grade = "C"
elif(60>=marks>50):
    grade = "D"
elif(marks<50):
    grade = "F"
print("Your grade is: ",grade)

#HW:7
post =input("Enter the post title: ")
# if(post.find("Harry")!= -1):
# if("harry" in post.lower()): # --> post.lower() will convert all post characters in lowercase.
if("Harry".lower() in post.lower()): # --> "Harry".lower() will convert "Harry" in its lowercase form viz. "harry".
    print("Post is related to Harry")
else: 
    print("Post is not related to Harry")
