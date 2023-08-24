import random

#CA1 Part 3
#Eryk Gloginski
#26/10/2021

#To get a random vaccine type from specified companies: AZ/MO/JA/PD
def vaccineType(num):
    #if the number equals to 1, 2, 3 or other, assign these as id and return it
    if num == 1:
        id = "AZ"
    elif num == 2:
        id = "MO"
    elif num == 3:
        id = "JA"
    else:
        id = "PF"
    return id

#getRandomStr() that will generate and return a string of 6 random digits (0 to 9).
def getRandomStr():
    #take a random integer from 0 to 9, convert it into a string and store it in d1 to d6 
    d1 = str(random.randint(0, 9))
    d2 = str(random.randint(0, 9))
    d3 = str(random.randint(0, 9))
    d4 = str(random.randint(0, 9))
    d5 = str(random.randint(0, 9))
    d6 = str(random.randint(0, 9))
    #store d1 to d6 in a list
    ranStr = [d1, d2, d3, d4, d5, d6]
    return ranStr

#Write a method called calcCheckDigit() that will compute and return the check digit for a
#random sequence passed as an argument.
def calcCheckDigit(listOfNums):
    #take from list listOfNums into d1 to d6 and convert from string to integer values
    d1 = int(listOfNums[0])
    d2 = int(listOfNums[1])
    d3 = int(listOfNums[2])
    d4 = int(listOfNums[3])
    d5 = int(listOfNums[4])
    d6 = int(listOfNums[5])
    #get the total of all values and turn it into a string
    total = (d6*1) + (d5*2) + (d4*3) + (d3*4) + (d2*5) + (d1*6)
    checkDigit = str(total)
    #return the last digit of the total which is the rightmost decimal
    return checkDigit[-1]

#Write a method generateCovidId() that will generate a random CovidCert id number of the
#form CCxxxxxxY where CC is one of the allowed vaccine values, x is a random digit and Y is the check
#digit. (Use the methods already written). The type of vaccine should be passed in as an argument.
def generateCovidId(vacType):
    #pass on variables to get the correct correct ID
    vaccineID = vaccineType(vacType)
    ranList = getRandomStr()
    checkNum = calcCheckDigit(ranList)
    #get the correct vaccination ID to go into a string and return it
    vacID = vaccineID
    for num in ranList:
        vacID = vacID + num
    vacID = vacID + checkNum
    return vacID

#Write a method validateCovidId() that will accept a CovidCert ID and will determine if it is
#valid or not.
def validateCovidId(covidID):
    #check if the length of the string is 9
    if len(covidID) == 9:
        #check if first two parts of the string are the correct type
        if covidID[0:2] == "AZ" or covidID[0:2] == "MO" or covidID[0:2] == "JA" or covidID[0:2] == "PF":
            #declare a testing list and fill it with 6 empty strings
            covidIdTest = [""] * 6
            for i in range(6):
                #populate list with type casted integer types from covidID
                covidIdTest[i] = int(covidID[2 + i])
            if calcCheckDigit(covidIdTest) == covidID[-1]:
                #check if the last digit is correct and if it is, return that it is valid
                return "Valid"
            else:
                return "Invalid (Check Digit)"
        else:
            return "Invalid (Invalid Type)"
    else:
        return "Invalid (Too Long/Short)"

#Part 3
#declare a basic list of CovidCertIDs and an empty testid string variable and print current IDs in list
vacIDs = ['AZ3093956', 'AZ5278513', 'MO2270351', 'MO3699476', 'JA4757500', 'JA3142378', 'PF2100472', 'PF5118730']
testid = ""
print(vacIDs)
#loop to add covid ids
while testid != "0":
    #take covid id into testid variable
    testid = input("Enter your VocidCertID to book a ticket (Enter 0 to Exit): ")
    #test if covidid is valid
    if validateCovidId(testid) == "Valid":
        #test if it is a duplicate entry, otherwise add it to vacIDs list
        if testid in vacIDs:
            print("Duplicate Entry! ")
        else:
            vacIDs.append(testid)
    else:
        print("Invalid CovidCertID:")

#print the list again and it should look different
print(vacIDs)



