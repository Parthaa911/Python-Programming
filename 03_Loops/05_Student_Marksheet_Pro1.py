# Write a pytho program to create a student marks calculator.
# 1. Accept marks of 5 subjects from the user.
# 2. Store all marks in a list.
# 3. Calculate the total marks using a while loop.
# 4. Calculate the percentage 
# 5. Display the students grade based on the percentage.

# Grade Criteria
# 90% and above - Grade  A
# 75% to 89% - Grade B
# 60% to 74% - Grade C
# 40% to 59% - Grade D
# Below  40% - Fail


subject=["C++","Python","Java","SQL","HTML"]
marks=[]

# Provding marks for each subject
for i in subject:
    mark=int(input(f"Enter marks of subject {i}:"))
    marks.append(mark)

#Calculating Total
    total = 0
    i = 0

while i < len(marks):
    total = total + marks[i]
    i = i + 1

#Calculating percentage 
percentage = total / 5

#Display result
print("Subject Marks:",marks)
print(f"Total: {total}/500")
print(f"Percentage:{percentage}%")


#Grade calculation
if percentage < 0 or percentage > 100:
    print("Invalid Percentage")

elif percentage >= 90:
    print("Grade: A")

elif percentage >= 75:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 40:
    print("Grade: D")

else :
    print("Fail")





