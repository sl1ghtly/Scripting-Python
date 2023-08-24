import random

questionsTotal = int(input("How many calculations in this test? "))
questions = questionsTotal
correct = 0

while questions != 0:
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    print("Multiplication of: ", num1, " and ", num2)
    answer = int(input("Enter the sum: "))
    if answer == num1 * num2:
        correct = correct + 1
    questions = questions - 1

print("You scored: ", correct, "/", questionsTotal)