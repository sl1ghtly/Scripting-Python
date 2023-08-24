str = input("enter any string of text: ")

#A
count = sum(1 for elem in str if elem.isupper())
print("number of capital letters", count)

#B
count = sum(1 for elem in str if elem.islower())
print("number of lower letters", count)

#C
vowels = 0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1

print("number of vowels: ", vowels)

#D
