def encrypt(subString, x):
    result = ""
    UserInput = input("Enter 1 to Encode. Enter 2 to Decode: ")

    # If the user decides to Encrypt message
    if (UserInput == "1"):
        for i in range(len(subString)):
            character = subString[i]
            # This if statement will Encrypt uppercase characters
            if (character.isupper()):
                result += chr((ord(character) + x - 65) % 26 + 65)
                # else it will Encrypt lowercase characters
            else:
                if (character == ' '):
                    character = ' '
                else:
                    result += chr((ord(character) + x - 97) % 26 + 97)
        return result

    # If the user decides to decrypt message
    if (UserInput == "2"):
        for i in range(len(subString)):
            character = subString[i]

            # This if statement will Decrypt uppercase characters
            if (character.isupper()):
                result += chr((ord(character) - x - 65) % 26 + 65)

                # else it will Decrypt lowercase characters
            else:
                if (character == ' '):
                    character = ' '
                else:
                    result += chr((ord(character) - x - 97) % 26 + 97)

        return result

# check the above function
# Read input and display results
subString = input("Enter your string: ")

x = 3
print ("Plain : " + subString)
print ("Cipher: " + encrypt(subString, x))
print ("Shift : " + str(x))