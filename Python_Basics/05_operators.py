#Operators
x=int(input("Enter First Number :")) # Convert String Value into Integer (Whole Number).
y=float(input("Enter Second  Number :")) # Convert String Value into Floating Point(Decimal Number).


# 1. Arithmatic Operators
print(f"\nAddition of {x} and {y} is {x+y}")
print(f"Subtraction of {x} and {y} is {x-y}")
print(f"Multiplication of {x} and {y} is {x*y}")
print(f"Division of {x} and {y} is {x/y}")
print(f"Floor division of {x} and {y} is {x//y}")
print(f"Modulus of {x} and {y} is {x%y}")
print(f"Power of {x} and {y} is {x**y}\n")


# 2. Comparison Operators
print("\nComparison Operators")
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 3. Logical Operators
print("\nLogical Operators")
print(x > 5 and x < 20)
print(x > 20 or x < 15)
print(not(x > 5))

# 4. Assignment Operators
print("\nAssignment Operators")
num = 10

num += 5
print("Num :",num)

num -= 3
print("Num :",num)

num *= 2
print("Num :",num)

# 5. Membership Operators
print("\nMembership Operators")
name = "Python"

print("P" in name)
print("z" not in name)

# 6. Identity Operators
print("\nIdentity Operators")
x = 10
y = 10

print(x is y)
print(x is not y)