def allTheSame(x, y, z):
    if x == y and x == z:
        return True
    else:
        return False

print(allTheSame(2,2,2))
print(allTheSame(2,2,3))

print()

def allDifferent(x, y, z):
    if x != y and x != z:
        return True
    else:
        return False

print(allDifferent(2,2,2))
print(allDifferent(2,2,3))
print(allDifferent(1,2,3))

def sorted(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

print(sorted(1,2,3))
print(sorted(3,2,1))
print(sorted(1,3,2))


