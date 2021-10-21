# Write a program that can encrypt and decrypt using the Affine Cipher.

from string import ascii_lowercase, ascii_uppercase

# Default lower aphabate i.e abcdefghijklmnopqrstuvwxyz
upper_alphabet = ascii_uppercase
# Default lower aphabate i.e ABCDEFGHIJKLMNOPQRSTUVWXYZ
lower_alphabet = ascii_lowercase

# The gcd function is going to help co-prime function
def gcd(a, b):
    # Everything divides 0
    if (a == 0 or b == 0):
        return 0
    # base case
    if (a == b):
        return a
    # a is greater
    if (a > b):
        return gcd(a - b, b)
    return gcd(a, b - a)


# Function to check if two numbers are co-prime or not
# retun True if co-prime else return false
def coprime(a, b):
    if (gcd(a, b) == 1):
        return True
    else:
        return False


"""
Purpose :   This function encrypt the pain text using Affine chiper
Input   :   message -> plain text which we want to encrpty
            key1 -> integer, must me co-prime of 26 and key to help encrypt plain text
            key2 -> integer , key to help encrypt plain text
output  :   return the encrypted text
Example :   message = information
            key1 = 17
            key2= 20
            then output = ahbyxqufayh
"""
def encrypt(message, key1, key2):
    encrypted_msg = ""

    # traverse text
    # and  applying encryption formula ( a x + b ) mod m
    for character in message:
        # Encrypt uppercase characters
        if character in upper_alphabet:
            new_char = (key1 * upper_alphabet.index(character) + key2) % len(upper_alphabet)
            encrypted_msg += upper_alphabet[new_char]
        # Encrypt lowercase characters
        elif character in lower_alphabet:
            new_char = (key1 * lower_alphabet.index(character) + key2) % len(lower_alphabet)
            encrypted_msg += lower_alphabet[new_char]
        # other than alphabet like digit , whitespace , symbol
        else:
            encrypted_msg += character
    return encrypted_msg

# function to find out modular multiplicative inverse of a number


def mod_inverse(num, mod_of):
    for x in range(1, mod_of):
        flag = (num*x) % mod_of
        # Check if (num*x)%26 == 1 ,then x will be the multiplicative inverse of num
        if flag == 1:
            return x


"""
Purpose :   This function encrypt the pain text using Affine chiper
Input   :   message -> plain text which we want to encrpty
            key1 -> integer, must me co-prime of 26 and key to help encrypt plain text
            key2 -> integer , key to help encrypt plain text
output  :   return the encrypted text
Example :   message = ahbyxqufayh
            key1 = 17
            key2= 20
            then ouput = information
"""
def decrypt(message, key1, key2):
    decrypted_msg = ""
    # Find key1^-1 (the multiplicative inverse of key1 in the group of integers modulo 26.)
    key_inverse = mod_inverse(key1, len(upper_alphabet))

    # traverse encrypted text
    # and Applying decryption formula a^-1 ( x - b ) mod m
    for character in message:
        # Encrypt uppercase characters
        if character in upper_alphabet:
            decrypt_char = ( key_inverse * (upper_alphabet.index(character) - key2)) % len(upper_alphabet)
            decrypted_msg += upper_alphabet[decrypt_char]
        # Encrypt lowercase characters
        elif character in lower_alphabet:
            decrypt_char = ( key_inverse * (lower_alphabet.index(character) - key2)) % len(lower_alphabet)
            decrypted_msg += lower_alphabet[decrypt_char]
        # other than alphabet like digit , whitespace , symbol
        else:
            decrypted_msg += character

    return decrypted_msg


# Driver code main
if __name__ == "__main__":
    while(True):
        while(True):
            try:
                key1 = int(
                    input("Enter the first key (must be co-prime of 26)"))
                if not (coprime(key1, len(lower_alphabet))):
                    print("First key must me coprime of 26")
                key2 = int(input("Enter the Second key : "))
                break
            except:
                print("Enter correct key!!\n")

        while(True):
            print("\n1. Encryption \n2. Decryption \n3. Change key \n4. Quit")
            choice = input("\nEnter your choice: ")

            if choice not in "1234":
                print("Invalid option, please enter a valid option")
            elif choice == "1":
                message = input("\nEnter the messaage: ")
                print("\nEncrypted message is : " +
                      encrypt(message, key1, key2))
            elif choice == "2":
                message = input("Enter the encrypted message: ")
                print("\nDecrypted message is : " +
                      decrypt(message, key1, key2))
            elif choice == "3":
                break
            elif choice == "4":
                exit(0)
