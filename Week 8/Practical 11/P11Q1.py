def copyFile(fileIn, fileOut):
    fIn = open(fileIn)
    fOut = open(fileOut, 'w')

    content = fIn.read()
    fOut.write(content)

    fIn.close()
    fOut.close()

def main():
    f1 = input("enter file name to copy: ")
    f2 = input("enter file name to copy to: ")
    copyFile(f1, f2)



main()