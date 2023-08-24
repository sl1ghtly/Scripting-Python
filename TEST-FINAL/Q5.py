results = [39, 100, 45, 56, 33, 89, 99, 40, 100, 55]
#a
count = 0
for result in results:
    if result == 100:
        count = count + 1

print("Number of students scoring 100%: ", count)
#b
results[9] = 75
print("Results list:", results)
#c
maximum = max(results)
print("Highest result is", maximum)
#d
minimum = min(results)
print("Lowest result is", minimum)
#e
average = sum(results) / len(results)
print("Average result is", average)
#f
results.sort()
print("Results list in order:", results)
#g
results.sort(reverse=True)
print("Results list reversed:", results)