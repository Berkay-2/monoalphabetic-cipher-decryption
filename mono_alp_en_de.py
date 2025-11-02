"""
Monoalphabetic Cipher Core Functions
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os
import random
import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def generate_key():
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return dict(zip(string.ascii_lowercase, letters))

def monoalphabetic_encrypt(text, key):
    result = []
    for char in text:
        if char.lower() in key:
            if char.isupper():
                result.append(key[char.lower()].upper())
            else:
                result.append(key[char])
        else:
            result.append(char)
    return ''.join(result)

def monoalphabetic_decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    result = []
    for char in ciphertext:
        if char.lower() in reverse_key:
            if char.isupper():
                result.append(reverse_key[char.lower()].upper())
            else:
                result.append(reverse_key[char])
        else:
            result.append(char)
    return ''.join(result)

def main():
    with open('../the_clockmaker_of_rothenburg.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    
    key = generate_key()
    
    # Encrypt
    encrypted = monoalphabetic_encrypt(text, key)
    with open('mono_encrypted.txt', 'w', encoding='utf-8') as f:
        f.write(encrypted)
    
    # Decrypt
    decrypted = monoalphabetic_decrypt(encrypted, key)
    with open('mono_decrypted.txt', 'w', encoding='utf-8') as f:
        f.write(decrypted)

if __name__ == "__main__":
    main()