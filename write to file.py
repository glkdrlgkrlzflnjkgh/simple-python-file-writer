# we don't need an 'import' here because python has file reading and writing functions built-in
string = "python is the BEST programming languege for  a beginner and it is VERY powerful!"
def WriteText(text) :
    file = open("test.txt",'w') #we need to open the file before doing anything to it
    print("opened file!")
    file.write(text) # write the 'text' argument of the 'WriteText' function to the opened file
    print("wrote", text , "to", file)
    print("closing file:", file) 
    file.close() #things could go VERY wrong if we don't do this
    print("finished writing to file!")
WriteText(string) #if you are modifying this; put this function caller AFTER the funcion code!
