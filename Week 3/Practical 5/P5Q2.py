total = 0
amount = 0
inputStr = input("Input Cash Amount (Q or q to stop): ")

while inputStr.upper() != "Q":
    value = float(inputStr)
    total += value
    amount = amount + 1
    inputStr = input("Input Cash Amount: ")

print("Total price: ", total)
print("Items purchased: ", amount)