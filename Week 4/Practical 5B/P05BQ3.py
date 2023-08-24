import random

num1 = random.randint(1, 12)
num2 = random.randint(1, 12)

chances = 3
guess = 0

while chances != 0 or guess != num1 + num2:
    print("Sum of: ", num1, " and ", num2)
    guess = int(input("Enter the sum: "))
    if guess == num1 + num2:
        print("Congratulations! ")
        break
    else:
        print("Try Again! ")