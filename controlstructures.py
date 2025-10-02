#Selection statements

#If statemeents 
#1.If-else statements 
#Provides an alternative code block when the if condition is False
print('''
1. VOTING ELIGIBILITY(If-else statements)
      ''')
age = 0
if age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#2.If-elif-else statements 
#For handling multiple, mutually exclusive conditions in a cascading manner
print('''
2. GRADES(If-elif-else statements)
      ''')
grade = 0
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


#3.Nested loops 
#If statements can be nested within other if, elif or else blocks to handle more complex conditional logic
print('''
3. GEAR SHIFT COMMANDS(Nested Loop)
      ''')
speed = 0
gearshift = False
if speed == 0:
    if gearshift:
        print("shift into the first gear")
    else:
        print("you are already in the first gear")
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


#Looping statements     
#1.For loop
#Execute code for each sequence
print('''
4. CAR LIST(For loop)
      ''')
#Iterating through a sequence
cars = ["BMW", "Benz", "Buggati", "Brabus"]
for car in cars: #Iterates all elements in the list
    print(f"I like {car}")

#Using Enumerate
#Provides both the index and the value during iteration. Useful for tasks requiring element position
print('''
5. CAR LIST(Enumerate Function)
      ''')
for index, value in enumerate(cars): 
    print(f"{index}: {value}")

#Using Range - Generates a sequence of numbers
print('''
6. NUMBERS(Range Function)
      ''')
#Range(Stop)- It starts from 0 but does not include the stop value
#Range(start, stop)- Starts from the start value up to the value before the stop value
#Range(start, stop, step)- Includes a step value
for i in range(0, 10, 3):
    print(i)


#2. While loops
#Execute code as long as a specified condition remains True 
#Condition-controlled loop- the loop continues until the condition becomes False 
print('''
7. COUNT(While loop)
      ''')
count = 0 
while count < 10: #Loops continues as long as count is less than 10
    print(f"count is: {count}")
    count += 1 #Crucial update to the condition variable to avoid infinite loop

#Infinite loops- occur if the condition never becomes false. 
#Must be handled carefully, often with break statements based on other conditions
print('''
8. USER_INPUT(Infinite loop)
      ''')
while True:
    user_input = int(input("Enter integer between 1 to 10: "))
    if user_input == 5:
        break# Exit the loop if condition is met 
