def readIntBtw(x, y):
    numList = []
    for i in range(x, y+1):
        numList.append(i)
    guess = -1
    while guess not in numList:
        guess = int(input("Enter a number between declared numbers: "))
        if guess not in numList:
            print("Number not in Range")
        else:
            print("Number in Range")
            exit()

readIntBtw(1, 12)
