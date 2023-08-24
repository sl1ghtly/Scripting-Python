number = int(input("Input number: "))
count = 1
for i in range(number):
    print(count, " ", end="")
    print(count * count, " ", end="")
    print(count * count * count, " ", end="")
    print()
    count = count + 1