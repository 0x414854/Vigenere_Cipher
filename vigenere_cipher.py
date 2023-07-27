import os

def vigenere_encrypt(message, key):
    table = {}
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(52):
        row = {}
        for j in range(52):
            row[letters[j]] = letters[(i+j) % 52]
        table[letters[i]] = row
    result = ""
    for i in range(len(message)):
        letter = message[i]
        if letter in table:
            key_letter = key[i % len(key)]
            if key_letter.isalpha():
                result += table[key_letter][letter]
        else:
            result += letter
    return result

def vigenere_decrypt(ciphertext, key):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        if letter.isalpha():
            key_letter = key[i % len(key)]
            if key_letter.isalpha():
                original_letter = letters[(letters.index(letter) - letters.index(key_letter)) % 52]
                result += original_letter
        else:
            result += letter
    return result


while True:
    choice = input("1. Encrypt\n2. Decrypt\nQ. Quit\nEnter your choice : ")
    if choice == '1':
        message = input("Enter the message to encrypt : ")
        key = input("Enter key: ")
        ciphertext = vigenere_encrypt(message, key)
        folder_path = "/Output/Path/for/Your/Encrypted/File/"
        file_name = input("Enter file name : ")
        file_path = os.path.join(folder_path, file_name + ".txt")
        with open(file_path, 'w') as file:
            file.write(ciphertext)
        print("The text has been encrypted and saved to the file : " + file_path)
    elif choice == '2':
        file_path = input("Enter the path of the file to decrypt : ")
        decryption_key = input("Enter decryption key : ")
        with open(file_path, 'r') as file:
            ciphertext = file.read()
        decrypted_message = vigenere_decrypt(ciphertext, decryption_key)
        print("Deciphered text : " + decrypted_message)
    elif choice.upper() == 'Q':
        print("\n See you soon !")
        break
    else:
        print("Error : Invalid entry, please try again.")

