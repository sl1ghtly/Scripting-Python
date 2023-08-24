def copyFile(fileIn, fileOut):
    fIn = open(fileIn)
    fOut = open(fileOut, 'a')

    content = fIn.read()
    fOut.write(content)

    fIn.close()
    fOut.close()

def main():
    f1 = input("enter file name to copy: ")
    
    copyFile(f1, 'other.txt')



main()