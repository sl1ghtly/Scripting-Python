digits = int(input("Input a 4 digit integer: "))

#first num
first = digits % 10

#second num
second = (digits // 10) %10

#third num
third = ((digits // 10) // 10) % 10

#fourth num
fourth = (((digits // 10) // 10) // 10) % 10

print("Reverse:", first, second, third, fourth)
