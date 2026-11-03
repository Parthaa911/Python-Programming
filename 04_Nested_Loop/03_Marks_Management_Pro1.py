# Write a Python program to create a Student Marks Management System using nested loops.

# The program should:
# 1. Accept the number of students from the user.
# 2. Accept each student's name.
# 3. Accept marks of 3 subjects for each student.
# 4. Calculate the total marks and percentage.
# 5. Display the student's grade based on the percentage.
# 6. Display Fail if the percentage is below 40%.
# 7. Check whether entered marks are valid (between 0 and 100).
# 8. Display the result of each student.

# Accept the number of students
students = int(input("Enter number of students: "))

# Outer loop for each student
for i in range(1, students + 1):

    print("\nStudent:", i)

    #Accept student name
    name = input("Enter student name: ")
    total = 0

    # Inner loop to accept marks of 3 subjects
    for j in range(1, 4):

        marks = int(input("Enter subject " + str(j) + " marks: "))

        # Check whether marks are valid
        if marks < 0 or marks > 100:
            print("Invalid Marks! Enter marks between 0 and 100.")
            break

        # Add subject marks to total
        total += marks

    else:
        #Calculate Percentage
        percentage = total / 3

        # Display student result
        print("\n===== Student Result =====")
        print("Name:", name)
        print("Total Marks:", total, "/300")
        print("Percentage:", round(percentage, 2), "%")

        # Display grade based on percentage
        if percentage >= 75:
            print("Grade: A")

        elif percentage >= 60:
            print("Grade: B")

        elif percentage >= 40:
            print("Grade: C")

        else:
            print("Result: Fail")

print("\nAll Student Results Completed!!")
