def countingwordsfromfile():

    filename=input("enter the file name")
    numbersofwords=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        numberofwords=numbersofwords+len(words)
    print("number of words")
    print(numberofwords)


countingwordsfromfile()        