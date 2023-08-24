import random

#CA1 Part 2
#Eryk Gloginski
#26/10/2021

#Part 1 Methods
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

#Part 2 Methods and Code
#Simple menu method
def menu():
    print("Choose a Vaccine type: ")
    print("1. AZ – AstraZeneca ")
    print("2. MO - Moderna ")
    print("3. JA - Janssen ")
    print("4. PF - Pfizer/BioNTech ")
    print("0. Exit ")

#Write a method that accepts a list as an argument and a vaccination type and
#returns a list of CovidCert IDs of given type.
def groupVaccineType(idList, vacType):
    #sets a count variable
    found = []
    #iterates through the list
    for id in idList:
        #checks if the id starts with AZ and if the is also equal to it
        if id[0:2] == "AZ" and vacType == "AZ":
            found.append(id)
        elif id[0:2] == "MO" and vacType == "MO":
            found.append(id)
        elif id[0:2] == "JA" and vacType == "JA":
            found.append(id)
        elif id[0:2] == "PF" and vacType == "PF":
            found.append(id)
    return found

#declare list and starter choice so while loop doesn't terminate
vacIDs = []
choice = -1

#loop to add covid ids to list
while choice != 0:
    #display menu and then ask for choice
    menu()
    choice = int(input("> "))
    #generate a covidid and save it to currentID variable for now
    currentID = generateCovidId(choice)
    #add to the list
    vacIDs.append(currentID)

#removes last false item from list when you press 0 to exit the loop
vacIDs.pop(-1)
#removes duplicates from list
vacIDs = list(dict.fromkeys(vacIDs))
print(vacIDs)

choice2 = ""
#loop to check amount of specified type of vaccine
while choice2 != "0":
    print("Enter a Vaccine Type (AZ, MO, JA or PF): ")
    choice2 = input("> ")
    typelist = groupVaccineType(vacIDs, choice2)
    if choice2 != "0":
        print("There is", len(typelist), "of the", choice2, "vaccine type! ")
        print(typelist)
    else:
        print("Exiting the program. ")
