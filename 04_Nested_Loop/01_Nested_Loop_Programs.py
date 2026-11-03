#Multiplication tables (1 to 5)

for i in range(1,11):

    for j in range(1,6):
        print(f"{j} X {i} = {i*j}",end="\t\t")

    print()


#Factors of numbers (1 to 10)

for i in range(1, 11):
    print("\nFactors of", i, ":")

    for j in range(1, i + 1):
        if i % j == 0:
            print(j, end=" ")

    print()

#Prime numbers (1 to 50)

for i in range(2, 51):
    count = 0

    for j in range(1, i + 1):
        if i % j == 0:
            count += 1

    if count == 2:
        print(i, end=" ")

#Common elements in  tow lists

list1=[2,9,3,7,1]
list2=[8,5,2,9,4]

print("Common Elements:")
for i in list1:
    for j in list2:
        if i==j:
            print(i)

#Number pairs (Sum = 10)

for i in range(1,6):
    for j in range(i, 10):
        if i + j == 10:
            print(i, "+", j, "=", i + j)
