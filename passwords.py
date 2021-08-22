import random

#creates alphanumeric password with special characters of the specified length
def alphaNum_withSymbols(length):
    i = 0
    output = ""
    while (i < length):
        output += str(chr(random.randint(33, 126))) #generates a random number (a single ASCII character that's allowed in passwords) and adds it to the string
        i+=1

    return output

#creates an alphanumeric password without any special symbols of the specified length
def alphaNum_noSymbols(length):
    i = 48
    index = 0
    noSpecial_list = [""]*62
    output = ""

    #these loops just build a list that doesn't have the special characters
    while(i <= 57):
        noSpecial_list[index] += str(chr(i))
        i+=1
        index+=1

    i = 65
    while(i <= 90):
        noSpecial_list[index] += str(chr(i))
        i+=1
        index+=1
 
    i = 97
    while(i <= 122):
        noSpecial_list[index] += str(chr(i))
        i+=1
        index+=1

    #forms the actual password
    i = 0
    while(i < length):
        output += noSpecial_list[random.randint(0, len(noSpecial_list) - 1)]
        i+=1

    return output