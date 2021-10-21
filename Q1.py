# Write a program that can encrypt and decrypt using the Additive Cipher.

from string import ascii_lowercase, ascii_uppercase

"""
Purpose :   This function encrypt the pain text using Additive chiper
Input   :   message -> plain text which we want to encrpty
            key -> integer, its key which tell how to charater shift
output  :   return the encrypted text
Example :   message = information
            key = 2
            then output = kphqtocvkqp
"""
def encrypt(message, key):
    encrypted_msg = ""
    # Default lower aphabate i.e abcdefghijklmnopqrstuvwxyz
    lower_alphabet = ascii_lowercase
    # Default lower aphabate i.e ABCDEFGHIJKLMNOPQRSTUVWXYZ
    upper_alphabet = ascii_uppercase

    # traverse text
    for character in message:
        # Encrypt uppercase characters
        if character in upper_alphabet:
            shift = (upper_alphabet.index(character) + key) % len(upper_alphabet)
            encrypted_msg += upper_alphabet[shift]
        # Encrypt lowercase characters
        elif character in lower_alphabet:
            shift = (lower_alphabet.index(character) + key) % len(lower_alphabet)
            encrypted_msg += lower_alphabet[shift]
        # other than alphabet like digit , whitespace , symbol
        else:
            encrypted_msg += character

    return encrypted_msg


"""
Purpose :   This function decrpty the encrypted text using Additive chiper
Input   :   message -> encrypted text which we want to decrpty
            key -> integer, its key which tell how to charater shift
output  :   return the encrypted text
Example :   message = kphqtocvkqp
            key = 2
            then output = information
"""
def decrypt(message, key):
    # call the encrypted function with negative key to decrypted the message
    return encrypt(message, -abs(key))


# Driver code main
if __name__ == "__main__":
    while(True):
        while(True):
            try:
                key = int(input("Enter the shift or key : "))
                break
            except:
                print("Enter correct shift!!\n")

        while(True):
            print("\n1. Encryption \n2. Decryption \n3. Change shift or key \n4. Quit")
            choice = input("\nEnter your choice: ")

            if choice not in "1234":
                print("Invalid option, please enter a valid option")
            elif choice == "1":
                message = input("\nEnter the messaage: ").lower()
                print("\nEncrypted message is : " + encrypt(message, key))
            elif choice == "2":
                message = input("Enter the encrypted message: ")
                print("\nDecrypted message is : " + decrypt(message, key))
            elif choice == "3":
                break
            elif choice == "4":
                exit(0)
