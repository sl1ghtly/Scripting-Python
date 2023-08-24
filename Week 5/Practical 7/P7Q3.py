def sumWithoutSmallest(listvar):
    smallest = listvar[0]
    for value in listvar:
        if value < smallest:
            smallest = value
    total = 0
    for value in listvar:
        total = total + value
    total = total - smallest
    return total

results = [39, 95, 45, 56, 33, 89, 99, 40, 95, 55]

print(sumWithoutSmallest(results))