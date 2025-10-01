#Selection statements

#If statemeents 
#If-else statements 
'''
VOTING ELIGIBILITY
'''
age = 17
if age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#If-elif-else statements 
print('''
      GRADES
      ''')
grade = 33
if grade >= 90: 
    print("Gade: A+")
elif grade >= 80:
    print("Grade: A")
elif grade >= 70:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
elif grade >= 50:
    print("Grade: D")
else:
    print("You failed, Grade: F")

#Nested loops 

print('''
GEAR SHIFT COMMANDS
      ''')
speed = 66
gearshift = True
if speed >= 0 and speed <= 10: 
    print("stay in the first gear")
elif speed >=10 and speed <=25:
    if gearshift: 
        print("shift into the second gear")
    else:
        print("you are already in the second gear")
elif speed >=25 and speed <=50:
    if gearshift: 
        print("shift into the third gear")
    else:
        print("you are already in the third gear")
elif speed >=50 and speed <=80:
    if gearshift: 
        print("shift into the fourth gear")
    else:
        print("you are already in the fourth gear")
elif speed > 80 :
    if gearshift: 
        print("shift into the fifth gear")
    else:
        print("you are already in the fifth gear")        
