def removeHighest(listvar):
    highest = listvar[0]
    for value in listvar:
        if value > highest:
            highest = value
    total = 0
    for value in listvar:
        total = total + value
    total = total - highest
    return total

results = [39, 95, 45, 56, 33, 89, 99, 40, 95, 55]

print(removeHighest(results))
