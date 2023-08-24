values = ['Aaa', 'Bbb', 'Ccc', 'Ddd', 'Aa', 'Bb', 'Cc', 'A', 'B']

shortest = len(values[0])
count = 0
for value in values:
    if shortest < len(value):
        shortest = value
    if shortest == len(value):
        count = count + 1

print("Shortest word: ", shortest)
print("Amount of words: ", count)