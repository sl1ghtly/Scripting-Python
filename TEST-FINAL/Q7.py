def countWinners(winList):
    counted = {i:winList.count(i) for i in winList}
    return counted

winners = ["St Eunan's", "Naomh Conaill", "Naomh Conaill", "Gaoth Dobhair", "Cill Cartha", 
"Glenswilly", "Naomh Conaill", "St Eunan's", "Glenswilly", "St Eunan's"]

print(countWinners(winners))