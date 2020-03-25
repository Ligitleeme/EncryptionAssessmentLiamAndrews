from Security import Security
import math, time, random

def getEncryptType():
    loop = True
    while loop == True:
        print("Which encryption method would you like to use?")
        encryptmode = input().lower()
        if encryptmode in ['caesar', 'c', 'polyalphabetic', 'p']:
            if encryptmode == 'caesar' or encryptmode == 'c':
                caesarcipher()
                loop = False
            else: 
                polyalphabetic()
                loop = False
        else:
            print('Enter either "caesar" or "c" or "polyalphabetic" or "p"')


def caesarcipher():
    Secure = Security()
    mode = Secure.getMode()
    f = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/" + Secure.getMessage())
    message = f.read()
    key = Secure.getKey()
    if mode == 'e' or mode == 'encrypt':
        translated = Secure.CaesarEncrypt(mode, message, key)
        f2 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/test.txt", "r")
        f3 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Caesar_Encrypted.txt", "w")
        f3.write(translated)
        f2.close()
        f3.close()
        print("Your file has been successfully encrypted to Caesar_Encrypted")
    if mode == 'd' or mode == 'decrypt':
        translated = Secure.CaesarDecrypt(mode, message, key)
        f2 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Caesar_Encrypted.txt", "r")
        f3 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Caesar_Decrypted.txt", "w")
        f3.write(translated)
        f2.close()
        f3.close()
        print("Your file has been successfully decrypted to Caesar_Decrypted")

def polyalphabetic():
    Secure = Security()
    mode = Secure.getMode()
    if mode == 'e' or mode =='encrypt':
        translated = Secure.PolySubEncryptor(mode)
        f5 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/test.txt" , "r")
        f5 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Polysub_Encrypted.txt" , "w")
        f5.write(translated)
        f5.close()
        print("Message encrypted and saved to Polysub_Encrypted ")

    if mode == 'd' or mode =='decrypt':
        translated = Secure.PolySubDecryptor(mode)
        f5 = open("c:/Users/ligit/Desktop/Techtorium/PyhtonAssesment/Polysub_Decrypted.txt" , "w")
        f5.write(translated)
        f5.close()
        print("Message decrypted and saved to Polysub_Decrypted ")

getEncryptType()