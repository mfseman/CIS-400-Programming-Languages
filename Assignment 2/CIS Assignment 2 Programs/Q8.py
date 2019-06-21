def Question8():
    import string

    fileName = ("C:/Users/Marco/Desktop/constitution.txt")
    File = open(fileName)
    # Creating a file to export my documentation to my local machine
    OutputFile = open("C:/Users/Marco/Desktop/count.dat","w")
    # Attempt to remove specific characters
    OtherValues = ['—', '”', '“']

    # Creating three arrays. the 1st array gathers the letters, the second array is for counting the amount
    # of times the character is used. the third array is to calculate the fequency and sort them
    list = []
    letterCount = []
    frequency = []

    # The total count of of the character used
    TotalCount = 0

    countCharacters = {}
    # A nested for loop that removes any whitespaces, digits, or punctuations
    for i in File: # search through the file and look at every character
        i = i.translate(str.maketrans('', '', string.punctuation)) # ignores punctuations: ()-'".:;
        i = i.translate(str.maketrans('', '', string.whitespace)) # ignores spaces
        i = i.translate(str.maketrans('', '', string.digits)) # ignores numeric values
        #i = i.translate(str.maketrans('', '', string.OtherValues)) # failed attempt
        # there wasnt a library for the other values which made it difficult to remove other values
        # such as: — ””
        i = i.lower() # doesn't matter if they are lower case or upper case

        # for loop that loops by each character, takes that letter and assign a number to it
        # based on the amount of times it was used.
        for letterCharacter in i:
            if letterCharacter in countCharacters:
                countCharacters[letterCharacter] += 1
            else:
                countCharacters[letterCharacter] = 1
    # For loop that counts the amount of times a specific character is used
    for characters, x in countCharacters.items():
        # Place zero as a place holder theen square the brackets to use the list that'll be modified
        list.append([x, characters, 0])
        letterCount.append(x)
    # calculates to total amount of times a character is used
    totalcount = sum(letterCount)
    #take the amount of times the character is used, then sort it by the amount of times how many times its used
    for y in letterCount:
        LetterFrequency = (y/totalcount) * 100
        frequency.append(LetterFrequency)
    frequency.sort(reverse=True)
    list.sort(reverse=True)

    # For loop that counts the entire character count so that i can divide it in the next loop
    for characters in list:
        TotalCount += characters[0]

    # Calculate the amount of times the character is used divide it by the total count
    for letter in list:
        decimalResult = (letter[0] / TotalCount)
        #Proper formatting of the decimal
        letter[2] += float(format(decimalResult, '.6f'))
# A for loop to print out all of the letters and frequency with the appropriate formatting
    for i in list:
        print('{} is {} '.format(i[1], i[2]))
        # Write all information to the dat file
        OutputFile.write('\n{} is {} '.format(i[1], i[2]))
    # Close out of the count.dat file
    OutputFile.close()
Question8()