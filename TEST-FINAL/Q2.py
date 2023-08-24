def repeat(text, n, delim):
    for i in range(n):
        print(text + delim, end="")


repeat("ho", 3, ", ")
print()
repeat("You will", 3, "! ")