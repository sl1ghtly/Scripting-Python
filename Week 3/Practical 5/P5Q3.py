inputStr = input("Enter a number 1-100 <Enter to end>: ")
largest = int(inputStr)
smallest = largest
passGrade = 0
failGrade = 0

while inputStr != "":
    value = int(inputStr)
    if value >= 0 or value <= 100:
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value
        if value >= 40:
            passGrade = passGrade + 1
        if value < 40:
            failGrade = failGrade + 1
        
    inputStr = input("Enter a number 1-100: ")
    
print("Largest is: ", largest)
print("Smallest is: ", smallest)
print("Amount of Passes: ", passGrade)
print("Amount of Fails: ", failGrade)