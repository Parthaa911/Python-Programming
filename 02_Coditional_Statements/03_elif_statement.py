# Take marks as input from the user and display the grade
marks = int(input("\nEnter your marks : "))
print("Marks :", marks)

if marks >= 90:
    print("O Grade")
elif marks >= 75:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
elif marks >= 45:
    print("C Grade")
elif marks >= 35:
    print("D Grade")
else:
    print("Fail (F)")

# Take temperature as input from the user and display the result(Hot/Normal/Cold)
temp = int(input("\nEnter Temperature : "))
print("Temperature :", temp)

if temp >= 40:
    print("Hot")
elif temp >= 20:
    print("Normal")
else:
    print("Cold")

# Take Age as input from the user and display the result(Child/Teenager/Adult/Senior Citizen)
age = int(input("\nEnter your Age : "))
print("Age :", age)

if age >= 60:
    print("You are Senior Citizen")
elif age >= 20:
    print("You are Adult")
elif age >= 13:
    print("You are Teenager")
elif age > 0 :
    print("You are Child")
else:
    print("Invalid Age")

