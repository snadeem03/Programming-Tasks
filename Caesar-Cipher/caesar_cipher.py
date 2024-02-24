import sys 

def encrypt(key, message):
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
                res = 97 + ((ascii + key) % 122)
                encrypted += chr(res)
            elif (ascii + key) <= 122:
                encrypted += chr(ord(letter) + key)
        else:
            encrypted += letter
    return encrypted
        
def decrypt(key, message):
    decrypted = ""
    for letter in message:
        type = check_letter(letter)
        if type == "upper":
            
            ascii = ord(letter)
            if (ascii - key) < 65:
                res = 91 - (65 - (ascii - key) - 1)
                decrypted += chr(res)
            else:
                decrypted += chr(ascii - key)
        elif type == "lower":
            ascii = ord(letter)
            if (ascii - key) < 97:
                res = 123 - (97 - (ascii - key) - 1)
                decrypted += chr(res)
            else:
                decrypted += chr(ascii - key)
        else:
            decrypted += letter
    return decrypted
        
def check_letter(letter):
    if letter.isupper():
        return "upper"
    elif letter.islower():
        return "lower"
        
def index(shift, message):
    if sys.argv[1] == "-e":
        return encrypt(shift, message)
    elif sys.argv[1] == "-d":
        return decrypt(shift, message)  
    else:
        print("Invalid option")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py [-e | -d] message shift")
        sys.exit(1)
    shift_key = int(sys.argv[3])
    message = sys.argv[2]
    print(index(shift_key, message))
