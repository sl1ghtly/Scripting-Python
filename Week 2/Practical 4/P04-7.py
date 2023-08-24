cost = float(input("Please enter the cost of your groceries: "))
points = 0
if (cost < 10):
    print("Points awarded: ", points, "(No Discount)")
elif (cost >= 10 and cost < 50):
    points = cost * 0.10
    print("Points awarded: ", points, "(10% Discount)")
elif (cost >= 50 and cost < 150):
    points = cost * 0.15
    print("Points awarded: ", points, "(15% Discount)")
elif (cost >= 150):
    points = cost * 0.20
    print("Points awarded: ", points, "(20% Discount)")
    

