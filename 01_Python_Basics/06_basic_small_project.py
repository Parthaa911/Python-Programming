print("------------Student Information------------")
name=input("Student Name :")  #Taking name as input
roll=int(input("Student Roll No. :"))  #Taking roll number as input

print("------------Student Marks------------")
#Taking marks as input
python=int(input("Python Marks :"))
java=int(input("Java Marks :"))
HTML=int(input("HTML Marks :"))

avg=(python+java+HTML)/3 # Calculating average marks

# Display Result 
print(f"\n--------- {name} Result --------")
print("Student Name :",name)
print("Student Roll No. :",roll)
print("\nSubject  Marks")
print("Python :",python)
print("Java   :",java)
print("HTML   :",HTML)
print("------------------")
print("Average:",avg)