#Right Triangle Star Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#Inverted Right Triangle Star Pattern
print()
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

#Number Triangle
print()
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#Inverted Number Triangle
print()
for i in range(5,0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print() 

#Pyramid Star Pattern

print()
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")

    print()
