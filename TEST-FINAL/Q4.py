def generateiFibTerm(nth):
    n1, n2 = 0, 1
    count = 0
    while count < nth:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

generateiFibTerm(10)