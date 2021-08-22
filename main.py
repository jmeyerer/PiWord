import csv
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


#pulls a random word from the word file
def randWord():
    with open("./4-letter-words.csv") as file:
        reader = csv.reader(file)
        temp = random.choice(list(reader))

    return str(temp)[2:6]


#creates a password of specified length with random words, no hyphens
def words_noHyphen(length):
    output = ""
    i = 1
    while (i <= length):
        output += randWord()
        i+=1

    return output


#creates a password with three random words separated by hyphens
def words_hyphen(length):
    output = ""
    i = 1

    while(i < length):
        output += randWord()
        output += "-"
        i+=1

    output += randWord()
    return output


#Super standard output, can be changed but not super necessary as it's not meant to be run all the time

print("")
print("")
print("-------------------------")
print("alphaNum_withSymbols(16)")
print(alphaNum_withSymbols(16))
print("-------------------------")

print("alphaNum_withSymbols(12)")
print(alphaNum_withSymbols(12))
print("-------------------------")

print("alphaNum_noSymbols(16)")
print(alphaNum_noSymbols(16))
print("-------------------------")

print("alphaNum_noSymbols(12)")
print(alphaNum_noSymbols(12))
print("-------------------------")

print("words_noHyphen(4)")
print(words_noHyphen(4))
print("-------------------------")

print("words_hyphen(4)")
print(words_hyphen(4))
print("-------------------------")
print("")
print("")