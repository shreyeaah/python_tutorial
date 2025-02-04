def encrypt(message, key):
    ciphertext = ""
    for ch in message:
        if 'a' <= ch <= 'z':  
            ordinal_ch = ord(ch)
            ordinal_ch += key
            if ordinal_ch > ord('z'):  
                ordinal_ch -= 26  
            new_ch = chr(ordinal_ch)
            ciphertext += new_ch
        else:
            ciphertext += ch  
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_message = ""
    for ch in ciphertext:
        if 'a' <= ch <= 'z':  
            ordinal_ch = ord(ch)
            ordinal_ch -= key
            if ordinal_ch < ord('a'):  
                ordinal_ch += 26  
            new_ch = chr(ordinal_ch)
            decrypted_message += new_ch
        else:
            decrypted_message += ch  
    return decrypted_message


message = input("Enter the message to encrypt: ").lower()  
key = int(input("Enter the shift key (integer): "))


ciphertext = encrypt(message, key)
print("Encrypted message:", ciphertext)


decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
