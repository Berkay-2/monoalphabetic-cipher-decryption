"""
Task 1: Affine Cipher
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os
import random
import time
from math import gcd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isupper():
            result += chr(((a * (ord(char) - 65) + b) % 26 + 65)
        elif char.islower():
            result += chr(((a * (ord(char) - 97) + b) % 26 + 97)
        else:
            result += char
    return result

def affine_decrypt(ciphertext, a, b):
    result = ""
    a_inv = modinv(a, 26)
    if a_inv is None:
        return "Invalid key"
    
    for char in ciphertext:
        if char.isupper():
            result += chr((a_inv * (ord(char) - 65 - b)) % 26 + 65)
        elif char.islower():
            result += chr((a_inv * (ord(char) - 97 - b)) % 26 + 97)
        else:
            result += char
    return result

def brute_force_affine(ciphertext):
    start_time = time.time()
    possible_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
    
    for a in possible_a:
        for b in range(26):
            decrypted = affine_decrypt(ciphertext, a, b)
            if "the" in decrypted.lower() and "and" in decrypted.lower():
                end_time = time.time()
                return (a, b), decrypted, end_time - start_time
    return None, None, time.time() - start_time

def main():
    try:
        with open('../the_clockmaker_of_rothenburg.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        
        possible_a = [a for a in range(1, 26) if gcd(a, 26) == 1]
        a = random.choice(possible_a)
        b = random.randint(1, 25)
        
        encrypted = affine_encrypt(text, a, b)
        with open('affine_encrypted.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted)
        
        decrypted = affine_decrypt(encrypted, a, b)
        with open('affine_decrypted.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted)
        
        key, hacked_text, time_taken = brute_force_affine(encrypted)
        with open('affine_hack_attempts.txt', 'w', encoding='utf-8') as f:
            f.write(f"Key: {key}\nTime: {time_taken:.2f}s\n\n{hacked_text}")
        
        print("Task1 completed successfully!")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
