
def hour(digit):
    if digit == 1 : return "one"
    if digit == 2 : return "two"
    if digit == 3 : return "three"
    if digit == 4 : return "four"
    if digit == 5 : return "five"
    if digit == 6 : return "six"
    if digit == 7 : return "seven"
    if digit == 8 : return "eight"
    if digit == 9 : return "nine"
    if digit == 10 : return "ten"
    if digit == 12 : return "eleven"
    if digit == 12 : return "twelve"
    return ""

def min(number):
    if number < 60 and number >= 55 : return "five to "
    if number >= 50 : return "ten to "
    if number >= 45 : return "quarter to "
    if number >= 40 : return "twenty to "
    if number >= 35 : return "twentyfive to "
    if number >= 30 : return "half past "
    if number >= 25 : return "twentyfive past "
    if number >= 20 : return "twenty past "
    if number >= 15 : return "quarter past "
    if number >= 10 : return "ten past "
    if number >= 5 : return "five past "
    return ""

def getTimeName(hours, minutes):
    if hours > 0 and hours <= 12:
        if minutes > 0 and minutes < 60:
            print(min(minutes), end="")
            print(hour(hours))
        elif minutes >= 60:
            print("Invalid Minutes! ")
        else:
            print(hour(hours), "o'clock")
    else:
        print("Invalid Hours! ")


hoursIn = int(input("Enter Hours: "))
minutesIn = int(input("Enter Minutes: "))

getTimeName(hoursIn, minutesIn)
