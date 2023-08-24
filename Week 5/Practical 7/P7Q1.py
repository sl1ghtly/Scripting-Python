results = [39, 95, 45, 56, 33, 89, 99, 40, 95, 55]
count = 0
for result in results:
    if result == 95:
        count = count + 1
print("Amount of 95%: ", count)

results[-1] = 65
print("Last Result: ", results[-1])

highest = 0
for result in results:
    if result > highest:
        highest = result
print("Highest: ", highest)

lowest = 100
for result in results:
    if result < lowest:
        lowest = result
print("Lowest: ", lowest)

avg = 0
for result in results:
    avg = avg + result
print("Average: ", avg / len(results))

results.sort()
print(results)

results.sort(reverse=True)
print(results)


