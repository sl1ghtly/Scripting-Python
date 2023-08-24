
time = int(input("Enter time in seconds: "))

minutes = time // 60
hLeft = minutes // 60
minLeft = minutes % 60
secLeft = time % 60

print("Time: ", hLeft, minLeft, secLeft)
