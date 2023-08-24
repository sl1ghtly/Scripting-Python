character = input("Input a character: ")

for i in range(6):
    for j in range(i):
        print(character, end="")
    print("")

for i in range(5, 0, -1):
    for j in range(i):
        print(character, end="")
    print("")

for i in range(6):
    for sp in range(6 - i):
        print(end=" ")
    for j in range(i):
        print(character, end="")
    print("")

for i in range(6):
    for sp in range(6 - i):
        print(end=" ")
    for j in range(i):
        print(character, end=" ")
    print("")