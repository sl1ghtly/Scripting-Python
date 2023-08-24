def smallest(x, y, z):
    tempSmall = x
    if x < y and x < z:
        tempSmall = x
    elif y < x and y < z:
        tempSmall = y
    else:
        tempSmall = z
    return tempSmall

print(smallest(7,8,9))

def average(x, y, z):
    avg = (x + y + z)/3
    return avg

print(average(7,8,9))
