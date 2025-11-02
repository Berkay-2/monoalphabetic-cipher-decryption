"""
Frequency Analysis Attack
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def frequency_analysis(ciphertext):
    # English letter frequency (from most to least common)
    english_freq = 'etaoinshrdlcumwfgypbvkjxqz'
    
    # Get frequency of letters in ciphertext
    counter = Counter(c.lower() for c in ciphertext if c.isalpha())
    sorted_letters = [letter for letter, count in counter.most_common()]
    
    # Create mapping
    mapping = {}
    for cipher_char, english_char in zip(sorted_letters, english_freq):
        mapping[cipher_char] = english_char
    
    return mapping

def decrypt_with_mapping(ciphertext, mapping):
    result = []
    for char in ciphertext:
        if char.lower() in mapping:
            if char.isupper():
                result.append(mapping[char.lower()].upper())
            else:
                result.append(mapping[char])
        else:
            result.append(char)
    return ''.join(result)

def main():
    with open('mono_encrypted.txt', 'r', encoding='utf-8') as f:
        ciphertext = f.read()
    
    mapping = frequency_analysis(ciphertext)
    decrypted = decrypt_with_mapping(ciphertext, mapping)
    
    with open('mono_oscar_guess_final.txt', 'w', encoding='utf-8') as f:
        f.write("Frequency Analysis Mapping:\n")
        for cipher, plain in sorted(mapping.items()):
            f.write(f"{cipher} -> {plain}\n")
        f.write("\nDecrypted Text:\n")
        f.write(decrypted)

if __name__ == "__main__":
    main()