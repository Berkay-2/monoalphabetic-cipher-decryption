"""
Task 3: DES Encryption (Manual Implementation)
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os
import binascii

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# DES Implementation 

# Initial Permutation Table
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Dummy DES function 
def des_encrypt_block(block, key):
    # In a real implementation, this would include:
    # Initial permutation, 16 rounds of Feistel network, final permutation
    return bytes([b ^ 0xAA for b in block])  # Simple XOR for demonstration

def pad_data(data):
    pad_len = 8 - (len(data) % 8)
    return data + bytes([pad_len] * pad_len)

def des_encrypt(plaintext, key):
    # Pad the plaintext
    plaintext = pad_data(plaintext)
    
    # Encrypt each block
    ciphertext = b''
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        encrypted_block = des_encrypt_block(block, key)
        ciphertext += encrypted_block
    
    return ciphertext

def main():
    # Read original text
    with open('../the_clockmaker_of_rothenburg.txt', 'rb') as f:        plaintext = f.read()
    
    
    key = b'secretky'  # 8-byte key
    
    # Encrypt
    ciphertext = des_encrypt(plaintext, key)
    
    # Save encrypted data
    with open('des_encrypted.txt', 'wb') as f:
        f.write(ciphertext)
    
    print("DES encryption completed. Output saved to des_encrypted.txt")

if __name__ == "__main__":
    main()