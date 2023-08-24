num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if (num1 == num2 and num1 == num3):
    print("All the Same")
elif (num1 != num2 and num1 != num3):
    print("All Different")
else:
    print("Neither")
