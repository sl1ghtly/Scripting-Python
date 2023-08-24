def sync(sets):
    s1 = sets[0]
    s2 = sets[1]
    s3 = sets[2]
    s4 = s1.union(s2.union(s3))
    return s4

def sync2(sets):
    fullset = set()
    for setname in sets:
        fullset = fullset.union(setname)
    return fullset


teamSheet1 = {"Mary", "Nuala", "Paddy", "Colm"}
teamSheet2 = {"Maeve", "Paddy", "Brendan", "Colm"}
teamSheet3 = {"Cliona", "Colm", "Brendan", "Nuala"} 

teamSheets = [teamSheet1, teamSheet2, teamSheet3]

playerNames = sync2(teamSheets)

print(playerNames)