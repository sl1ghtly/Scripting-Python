text = input("Enter a word: ")

textLen = len(text)
half = textLen // 2

if (textLen % 2 == 0):
    print("divisible by 0")
    print(text[half-1:half+1])
else:
    print("not divisible by 0")
    print(text[half:half+1])


