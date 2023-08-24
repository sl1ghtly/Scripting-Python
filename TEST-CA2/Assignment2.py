import random
import csv

def menu():
    # simple menu
    print()
    print("1. Display contents of any csv file on screen")
    print("2. Display contents of any text file on screen")
    print("3. Select a key word")
    print("4. Generate an encryption string")
    print("5. Encrypt a file")
    print("6. Decrypt a file")
    print("7. Quit")
    print()

def encode(filename, keyword):
    # if filename doesn't contain ".txt" or ".csv"
    try:
        name, file_format = filename.rsplit(".", 1)
        if file_format not in ["txt", "csv"]:
            raise Exception("File format not supported: txt and csv only.")
    except ValueError:
        print("Value Error: Cannot split file name.")
    except UnboundLocalError:
        print("Unbound Local Error: Variable not assigned.")
    except Exception as e:
        print(e)

    # if it doesn't have 'Enc' in filename (so basically encoding)
    if "Enc" not in filename[-7:]:
        try:
            new_filename = name + "Enc." + file_format
        except UnboundLocalError:
            print("Unbound Local Error: Cannot create new file name.")
        try:
            with open(filename) as fp:
                # read text from file in small letters, take keyword and remove duplicates and create the encoderKey
                text = fp.read().lower()
                # removes duplicate chars from string in order (shown to me by a friend with years of experience)
                keyword = "".join(dict.fromkeys(keyword))
                encoderKey = buildEncryptionStr(keyword)
                # assign s=>a, c=>b, r=>c etc... (using "scripting" example)
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                # quick dirty fix so there's no exception when converting stuff that's not specified
                # like numbers, new lines, dots, commas etc.
                encoder = {' ':' ', '.':'.',',':',','!':'!','?':'?',';':';',':':':','<':'<','>':'>','-':'-','_':'_','–':'–','+':'+','"':'"',"'":"'",'@':'@','\n':'\n','(':'(',')':')','{':'{','}':'}','[':'[',']':']','£':'£','$':'$','%':'%','^':'^','&':'&','*':'*','~':'~','#':'#'}
                for i in range(10):
                    encoder[i] = i
                for i in range(len(alphabet)):
                    encoder[alphabet[i]] = encoderKey[i]
                # encode the text
                textEncoded = ""
                for i in range(len(text)):
                    textEncoded += encoder[text[i]]
                # finally write encoded text to file and return encoderKey
                finishFile = open(new_filename, "w")
                finishFile.write(textEncoded)
                finishFile.close()
                print("Your file has been encrypted. Your key is:", encoderKey)
                return encoderKey
        except FileNotFoundError:
            print("File Not Found Error: File does not exist.")
        # if it does have 'Enc' in filename (so basically decoding)
    else:
        new_filename = name[:-3] + "V1." + file_format
        try:
            with open(filename) as fp:
                # read text from file in small letters, take keyword set it as decoderKey
                text = fp.read().lower()
                decoderKey = keyword
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                # quick dirty fix so there's no exception when converting stuff that's not specified
                # like numbers, new lines, dots, commas etc.
                decoder = {' ':' ', '.':'.',',':',','!':'!','?':'?',';':';',':':':','<':'<','>':'>','-':'-','_':'_','–':'–','+':'+','"':'"',"'":"'",'@':'@','\n':'\n','(':'(',')':')','{':'{','}':'}','[':'[',']':']','£':'£','$':'$','%':'%','^':'^','&':'&','*':'*','~':'~','#':'#'}
                for i in range(10):
                    decoder[i] = i
                for i in range(len(alphabet)):
                    decoder[decoderKey[i]] = alphabet[i]
                # decode the text
                textDecoded = ""
                for i in range(len(text)):
                    textDecoded += decoder[text[i]]
                # finally write decoded text to file and return file name
                finishFile = open(new_filename, "w")
                finishFile.write(textDecoded)
                finishFile.close()
                print("Your file has been decrypted. Your file is saved in:", new_filename)
                return new_filename
        except FileNotFoundError:
            print("File Not Found Error: File does not exist.")

def getWordListFromFile(filename):
    # get file and turn it into a list by splitting the entire contents
    try:
        file = open(filename, "r")
        words = file.read().lower().split(" ")
        keys = []
        disallowed = [' ','.',',','!','?',';',':','<','>','-','_','–','+','"',"'",'@','\n','(',')','{','}','[',']','£','$','%','^','&','*','~','#']
        # check if each word is has a length of 7 or bigger and add to keys
        # or if it accidentally contains a disallowed character
        for word in words:
            good = True
            for c in word:
                if c in disallowed:
                    good = False
            if good:
                if len(word) >= 7:
                    keys.append(word)
        file.close()
        return keys
    except FileNotFoundError:
        print("File Not Found Error: File does not exist.")
        
def selectRandomKey(keylist):
    # cool method that returns 1 keyword of the keylist
    try:
        ranKey = random.choice(keylist)
        return ranKey
    except TypeError:
        print("Type Error: Object has no length.")
    
def buildEncryptionStr(keyword):
    # alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    testKey = keyword + alphabet[::-1]
    testKey = list(testKey)
    encoderKey = ""
    # convert testKey into encoderKey
    for c in testKey:
        if c not in encoderKey:
            encoderKey = encoderKey + c
    return encoderKey

choice = "0"
while(choice != "7"):
    menu()
    choice = input("> Enter your choice: ")
    # display csv file contents
    if choice == "1":
        csvfile = input("> Enter the csv filename to open: ")
        if ".csv" not in csvfile:
            print("File format not supported: csv only.")
        try:
            file = open(csvfile, "r")
            csvreader = csv.reader(file)
            header = next(csvreader)
            print(header)
            rows = []
            for row in csvreader:
                rows.append(row)
            print(rows)
            file.close()
        except FileNotFoundError:
            print("Error, file does not exist!")
    # display txt file contents
    elif choice == "2":
        txtfile = input("> Enter the txt filename to open: ")
        if ".txt" not in txtfile:
            print("File format not supported: txt only.")
        try:
            file = open(txtfile, "r")
            print(file.read())
            file.close()
        except FileNotFoundError:
            print("Error, file does not exist!")
    # select key
    elif choice == "3":
        fn = input("> Enter file name to look for a random key: ")
        keylist = getWordListFromFile(fn)
        keyword = selectRandomKey(keylist)
        print("Your keyword from the list of words is:", keyword)
    # build encryption key
    elif choice == "4":
        kw = input("> Enter a word that's at least 7 words: ")
        encryptString = buildEncryptionStr(kw)
        print("Your encryption string is:", encryptString)
    # encrypt
    elif choice == "5":
        fn = input("> Enter a filename to encrypt(filename.*): ")
        keylist = getWordListFromFile(fn)
        key = selectRandomKey(keylist)
        encodeKey = encode(fn, key)
    # decrypt
    elif choice == "6":
        fn = input("> Enter a filename to decrypt(filenameEnc.*): ")
        dk = input("> Enter your decrypt key: ")
        new_file = encode(fn, dk)
    # quit the program
    elif choice == "7":
        print("Exiting the program...")
        quit()
    else:
        print("Invalid Option. Choose between 1 to 7. ")
