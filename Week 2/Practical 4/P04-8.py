cost = float(input("Enter Price Paid for Meal: "))
satisfaction = int(input("Enter Satisfaction Level (1-3): "))
tip = 0

if (satisfaction == 1):
    tip = cost * 0.20
elif (satisfaction == 2):
    tip = cost * 0.15
elif (satisfaction == 3):
    tip = cost * 0.10

print("Price: $", cost, " Satisfaction Level: ", satisfaction, " Tip: $", tip)
