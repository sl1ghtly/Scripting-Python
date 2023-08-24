def removeDups(dupsList):
    return list(dict.fromkeys(dupsList))

results = [39, 100, 45, 56, 33, 89, 99, 40, 100, 55]
print(removeDups(results))
