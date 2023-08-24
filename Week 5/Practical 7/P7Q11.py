values = ['ll', 'mm', 'mn', 'nn', 'no', 'oo']
newvalues = []

for value in values:
    if value[0] == 'm' or value[0] == 'n':
        newvalues.append(value)

print(values)
print(newvalues)
