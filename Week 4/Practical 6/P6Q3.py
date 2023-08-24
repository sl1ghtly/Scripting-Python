#fourth = (((digits // 10) // 10) // 10) % 10
def firstDigit(n):
    first = str(n)
    return first[0]

print(firstDigit(1729))

def lastDigit(n):
    last = n % 10
    return last

print(lastDigit(1729))

def digits(n):
    string = str(n)
    amount = len(string)
    return amount

print(digits(1729))