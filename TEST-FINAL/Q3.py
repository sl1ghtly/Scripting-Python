def getValueInRange(int1, int2):
    value = -1
    while value not in range(int1, int2):
        value = int(input(">Enter a value:"))
        if (value > int2 or value < int1):
            print("Value not in range! ")
        else:
            print("Value", value, "in range of", int1, "and", int2, "! ")

getValueInRange(0,59)
getValueInRange(0,100)
    
