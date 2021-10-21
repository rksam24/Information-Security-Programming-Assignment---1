# Write a program that can encrypt and Decrypt using a 2 X 2 Hill Cipher
# pip install numpy

from string import ascii_lowercase
import numpy as np


# Default lower aphabate i.e abcdefghijklmnopqrstuvwxyz
alphabet = ascii_lowercase+" "
# size of key matrix example  if keySize=2 the key_matrix is of 2x2 matrix
keySize = 2

"""
Purpose :   Function used to generate key matrix which use for encrpty and decrypt text
            according to key size if keySize=2 the key_matrix is of 2x2 matrix
Input   :   key -> string , used to generate key matrix
Output  :   return key matrix
"""
def generate_key_marix(key):
    key_matrix = [[0]*keySize for _ in range(keySize)]
    k = 0
    for i in range(keySize):
        for j in range(keySize):
            key_matrix[i][j] = alphabet.index(key[k])
            k += 1
    return key_matrix


"""
Pupose  :   Function used to convert text into martix(that has been mapped to numbers) and split it in correct size
Input   :   message -> Text which hab been mapped to number then convert into martix and then split into matrix of keysize x 1
Ouput   :   return matrix which is mapped according to message
"""
def text_to_matrix(messaage):
    messaage_in_number = [alphabet.index(char) for char in messaage]
    messaage_matrix = [messaage_in_number[i:i + keySize]
                       for i in range(0, len(messaage_in_number), keySize)]
    return messaage_matrix


"""
Purpose :   Convert the matrix into text
Input   :   matrix  -> matrix which we want to convert
Output  :   return converted text
"""
def matrix_to_text(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text += alphabet[matrix[i][j]]
    return text


"""
Purpose :   Function to encrypt plain text using Hill chiper
Input   :   meassge -> plain text matrix to encrypt
            key ->  key matrix which used to encrypt
Ouput   :   return encrypted text
"""
def encrypt(message, key):
    # convert text to matrix
    message = text_to_matrix(message)

    encrypted_message = list()

    # iterate through each partial message
    # encryt using (K*P)mod26
    for P in message:
        # P = Vector of plaintext (that has been mapped to numbers)
        while len(P) != len(key):
            P.append(alphabet.index(" "))
        P = np.transpose(np.asarray(P))

        encrypted_message.append(np.dot(key, P) % len(alphabet))

    # convert into text and return it
    return matrix_to_text(encrypted_message)


"""
Purpose :   Find the matrix modulus inverse by
            Step 1) Find determinant
            Step 2) Find determinant value in a specific modulus (usually length of alphabet)
            Step 3) Take that det_inv times the det*inverted matrix (this will then be the adjoint) in mod 26
Input   :   matrix  -> which whose matrix modulus inverse we want to find
            mod -> specific modulus (usually length of alphabet)
Output  :   return martix modulus inverse of given matrix
"""
def matrix_mod_inverse(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # step 1
    # step 2
    det_inv = mod-1
    for x in range(1, mod+1):
        flag = (det*x) % mod
        if flag == 1:
            det_inv = x
            break
    matrix_modulus_inverse = det_inv * \
        np.round(det*np.linalg.inv(matrix)).astype(int) % mod  # step 3
    return matrix_modulus_inverse


"""
Purpose :   Function to decrypt encrypted text using Hill chiper
Input   :   meassge -> plain text matrix to encrypt
            key ->  key matrix which used to encrypt
Ouput   :   return encrypted text
"""
def decrypt(message, key):
    # convert text to matrix
    message = text_to_matrix(message)

    decrypted_message = list()

    # Find K_inverse (the matrix modulus inverse of key with modulus 26)
    K_inv = matrix_mod_inverse(key, len(alphabet))

    # iterate through each partial chiper text
    # decrypt using inv(K)*C mod 26
    for C in message:
        # C = Vector of Ciphered text (in numbers)
        C = np.transpose(np.asarray(C))
        decrypted_message.append(np.dot(K_inv, C) % len(alphabet))

    # Convert dechipered matrix into text and return it
    return matrix_to_text(decrypted_message)


# Driver Code Main
if __name__ == "__main__":
    while(True):
        while(True):
            key = input("Enter the key (length of key must be {}): ".format(
                keySize*keySize)).lower()
            if len(key) == keySize*keySize:
                break
            else:
                print("Enter correct key")
        key = generate_key_marix(key)
        while(True):
            print("\n1. Encryption \n2. Decryption \n3. Change key \n4. Quit")
            choice = input("\nEnter your choice: ")

            if choice not in "1234":
                print("Invalid option, please enter a valid option")
            elif choice == "1":
                message = input("\nEnter the messaage: ").lower()
                print("\nEncrypted message is : " + encrypt(message, key))
            elif choice == "2":
                message = input("Enter the encrypted message: ").lower()
                print("\nDecrypted message is : " + decrypt(message, key))
            elif choice == "3":
                break
            elif choice == "4":
                exit(0)
