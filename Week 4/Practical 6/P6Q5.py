def countVowels(s):
    vowels = 0
    for i in s:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels = vowels+1
    return vowels

print(countVowels("This string of TEXT is a TEST"))