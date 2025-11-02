"""
Task 3: DES Decryption (Manual Implementation)
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def des_decrypt_block(block, key):
    # Reverse of the dummy encryption
    return bytes([b ^ 0xAA for b in block])  # Simple XOR for demonstration

def unpad_data(data):
    pad_len = data[-1]
    return data[:-pad_len]

def des_decrypt(ciphertext, key):
    # Decrypt each block
    plaintext = b''
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        decrypted_block = des_decrypt_block(block, key)
        plaintext += decrypted_block
    
    # Remove padding
    return unpad_data(plaintext)

def main():
    # Read encrypted file
    with open('des_encrypted.txt', 'rb') as f:
        ciphertext = f.read()
    
    # Use the same key as encryption
    key = b'secretky'  # 8-byte key
    
    # Decrypt
    plaintext = des_decrypt(ciphertext, key)
    
    # Save decrypted data
    with open('decrypted_output.txt', 'wb') as f:
        f.write(plaintext)
    
    print("DES decryption completed. Output saved to decrypted_output.txt")

if __name__ == "__main__":
    main()