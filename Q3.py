"""
Write a program that can perform a letter frequency attack on an additive cipher without human intervention. 
Your software should produce possible plain text in rough order of likelihood. It would be good if your user 
interface allows user to specify " Give me top 10 possible plain texts
"""

from string import ascii_lowercase

"""
Purpose :   Function to decrypt a additive cipher using the letter frequency attack
Input   :   encrypted_msg -> encrypted text which we want to decrypt
            no_of_outcome -> total number of top possible plain texts we want
Ouput   :   a list contain all possbile plain text
"""
def letter_frequency_attaack(encrypted_msg, no_of_outcome):
    # Default lower aphabate i.e abcdefghijklmnopqrstuvwxyz
    alphabet = ascii_lowercase

    # Store the frequency of each letter in encrypted text
    freq = [0] * len(alphabet)

    # Stores the frequency of each letter in encrypted text in descending order
    freq_sorted = [0]*len(alphabet)

    # Store which alphabet is used already
    used_alphabet = [0] * len(alphabet)

    #  Stores all final possible deciphered plaintext
    plain_text = list()

    # Traverse encrypted text
    # and find frequency of each chiper text
    # whitespace, symbol and digit are not included
    for char in encrypted_msg:
        if char in alphabet:
            freq[alphabet.index(char)] += 1
            freq_sorted[alphabet.index(char)] += 1

    # Sort the frequency in descending order
    freq_sorted.sort(reverse=True)

    # letter frequenty used in english language
    frequenty_used = "etaoinshrdlcumwfgypbvkjxqz"

    # Itearate for all possible outcome
    for i in range(no_of_outcome):
        # Iterate over the range [0, 26]
        for j in range(len(alphabet)):
            if freq_sorted[i] == freq[j] and used_alphabet[j] != 1:
                # letter 'e' used most in english letter so we used 'e' letter to find key to decrpty encrypted text
                key = j - alphabet.index(frequenty_used[i])
                used_alphabet[j] = 1

        # Temporary string to generate one plaintext at a time
        current_text = ""

        # Generate the probable ith plaintext
        # string using the key calculated above
        for char in encrypted_msg:
            if char in alphabet:
                shift = (alphabet.index(char) - key) % len(alphabet)
                current_text += alphabet[shift]
            else:
                current_text += char

        plain_text.append(current_text)

    return plain_text


# Driver code main
if __name__ == "__main__":
    encrypted_msg = input("Enter the encrypted message:\n").lower()
    while(True):
        try:
            no_of_possible_ouput = int(
                input("\nEnter the number of possible text: "))
            break
        except:
            print("Enter correct number of possible text")

    print("\nPossible Plan text are : \n")
    plain_txt = letter_frequency_attaack(encrypted_msg, no_of_possible_ouput)

    for txt in plain_txt:
        print(txt+"\n\n")
