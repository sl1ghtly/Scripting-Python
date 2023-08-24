values = ['Aaa', 'Bbb', 'Ccc', 'Ddd', 'Eee', 'Aa', 'Bb', 'Cc', 'Dd', 'A', 'B', 'C']

letter = 'D'
count = 0
for value in values:
    if letter == value[0]:
        count = count + 1

print("Amount of letter", letter, " in list: ", count)