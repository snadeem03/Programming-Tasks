
import sys
# rot13 encryption
def encrypt(message):
    key=13
    
    encrypted = ""
    for letter in message:
        type = check_letter(letter)
        if type == "upper":
            ascii = ord(letter)
            if (ascii + key) > 90:
                res = 64 + ((ascii + key) % 90)
                encrypted += chr(res)
            elif (ascii + key) <= 90:
                encrypted += chr(ord(letter) + key)
        elif type == "lower":
            ascii = ord(letter)
            if (ascii + key) > 122:
                res = 96 + ((ascii + key) % 122)
                encrypted += chr(res)
            elif (ascii + key) <= 122:
                encrypted += chr(ord(letter) + key)
        else:
            encrypted += letter
    return encrypted


# rot13 decryption
def decrypt(message):
    key=13
    
    decrypted = ""
    for letter in message:
        type = check_letter(letter)
        if type == "upper":

            ascii = ord(letter)
            if (ascii - key) < 65:
                res = 90 - (65 - (ascii - key) - 1)
                decrypted += chr(res)
            else:
                decrypted += chr(ascii - key)
        elif type == "lower":
            ascii = ord(letter)
            if (ascii - key) < 97:
                res = 122 - (97 - (ascii - key) - 1)
                decrypted += chr(res)
            else:
                decrypted += chr(ascii - key)
        else:
            decrypted += letter
    return decrypted

# checking the case of the letter
def check_letter(letter):
    if letter.isupper():
        return "upper"
    elif letter.islower():
        return "lower"

# checking the options
def index(message):
    if sys.argv[1] == "-e":
        return encrypt(message)
    elif sys.argv[1] == "-d":
        return decrypt(message)
    else:
        print("Invalid option")
        sys.exit(1)
        
        
        
if __name__ == "__main__":
    message=sys.argv[2]
    print(index(message))    
    