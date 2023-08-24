sub1 = "Python"
sub2 = "Mathematics"
sub3 = "Computer Science"

name = input("Enter Student name: ")
sub1Res = float(input("Enter result for " + sub1 + ": "))
sub2Res = float(input("Enter result for " + sub2 + ": "))
sub3Res = float(input("Enter result for " + sub3 + ": "))

print(name)
print(sub1 + ":      %.1f" % sub1Res)
print(sub2 + ":      %.1f" % sub2Res)
print(sub3 + ":      %.1f" % sub3Res)


print()
print("%-20s:%8.1f" %  (sub1,sub1Res))
print("%-20s:%8.1f" %  (sub2,sub2Res))
print("%-20s:%8.1f" %  (sub3,sub3Res))
#print(sub2 + ":      %.1f" % sub2Res)
#print(sub3 + ":      %.1f" % sub3Res)
