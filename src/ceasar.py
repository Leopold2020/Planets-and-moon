def encrypt(text, key):
    """ceasarchifferskryptering
    
    args:
        text(_str_): den som ska krypteras.
        key(_int_): Hur många steg ska vi skifta?
    """
    encrypted = ""
    #loop through the message char by char
    for char in text:
        #check if it's an upper case letter
        if char.isupper():
            char_index = ord(char) - ord ('A')


            char_shifted = (char_index + key) % 26 + ord('A')
            char_new = chr(char_shifted)
            encrypted += char_new

        elif char.islower():
            char_index = ord(char) - ord('a')


            char_shifted = (char_index + key) % 26 + ord('a')
            char_new = chr(char_shifted)
            encrypted += char_new

        elif char.isdigit():
            char_new =(int(char) + key) % 10
            encrypted += str(char_new)


        else:
            encrypted += char

    return encrypted

def unencrypt(text, key):
    """ceasarchifferskryptering
    
    args:
        text(_str_): den som ska krypteras.
        key(_int_): Hur många steg ska vi skifta?
    """
    unencrypted = ""
    #loop through the message char by char
    for char in text:
        #check if it's an upper case letter
        if char.isupper():
            char_index = ord(char) - ord ('A')


            char_unshifted = (char_index - key) % 26 + ord('A')
            char_new = chr(char_unshifted)
            unencrypted += char_new

        elif char.islower():
            char_index = ord(char) + ord('a')


            char_unshifted = (char_index - key) % 26 + ord('a')
            char_new = chr(char_unshifted)
            unencrypted += char_new

        elif char.isdigit():
            char_new =(int(char) - key) % 10
            unencrypted += str(char_new)


        else:
            unencrypted += char

    return unencrypted



def main():
    message = "Hello, i was wondering what 69 means?"
    encrypted_message = encrypt(message, 1)
    print(f"Message: {message}")
    print(f"Encrypted message with 1 shift: {encrypted_message}")
    message2 = unencrypt(encrypted_message, 1)
    print(f"{message2}")




if __name__ == "__main__":
    main()