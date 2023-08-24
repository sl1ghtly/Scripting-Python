str = input("enter any string of text: ")

#A
upper = ""
for i in str:
    if i.isupper():
        upper += i

print(upper)

#B
str2 = ""
for i in range(len(str)):
    if (i%2)==0:
        str2+=str[i]

print(str2)

#C
new_str = ""
vowels = "aeiouAEIOU"
for letter in str:
    if letter in vowels:
        new_str += '_'
    else:
       new_str += letter

print(new_str)

#D
for i, char in enumerate(str):
    if char in vowels:
        print(char, i)
