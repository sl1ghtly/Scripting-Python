count = 0
count2 = 0
count3 = 0
total = 0
total2 = 0
total3 = 0
n = 100

#A
while total < n:
    total = count * count
    count = count + 1
    print(total)

#B
while total2 < n:
    total2 = count2 * 10
    print(total2)
    count2 = count2 + 1

#C
while total3 < n:
    total3 = pow(2, count3)
    print(total3)
    count3 = count3 + 1