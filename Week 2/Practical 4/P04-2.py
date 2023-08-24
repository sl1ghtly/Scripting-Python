num = float(input("Enter an integer: "))

if (num == 0):
    print("Zero")
elif (num > 0):
    print("Positive")
else:
    print("Negative")
if (num > 1000000 or num < -1000000):
    print("Large")
elif (num < 1 and num > -1):
    print("Small")
