hours = 0
mins = 0

while hours < 24 :   
   mins = 0
   while mins < 60 :
      print("%02d:%02d " % (hours , mins))
      mins+=1
   hours+=1

for hours in range(24):
   for mins in range(60):
      print("%02d:%02d " % (hours , mins))
    
