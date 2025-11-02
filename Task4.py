"""
Task 4: DES CFB Mode
Student: Abdullah Berkay Kürkçü
Matriculation Number: 67909114
"""

import os
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import subprocess
import binascii

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def run_des_cfb():
    try:
        print("Starting DES CFB encryption...")
        
        # 1. Verify text file exists
        text_path = os.path.join(os.path.dirname(__file__), '../../the_clockmaker_of_rothenburg.txt')
        if not os.path.exists(text_path):
            raise FileNotFoundError("the_clockmaker_of_rothenburg.txt not found in parent directory")
        
        # 2. Read plaintext
        with open(text_path, 'rb') as f:
            plaintext = f.read()
        print(f"Read {len(plaintext)} bytes from source file")
        
        # 3. Generate random key and IV
        key = os.urandom(8)  # DES uses 56-bit key (8 bytes)
        iv = os.urandom(8)   # Initialization vector
        print(f"Generated key: {binascii.hexlify(key).decode()}")
        print(f"Generated IV: {binascii.hexlify(iv).decode()}")
        
        # 4. Encrypt using DES CFB
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
        encrypted = cipher.encrypt(pad(plaintext, DES.block_size))
        
        # 5. Save encrypted file
        with open('des_cfb_encrypted.bin', 'wb') as f:
            f.write(encrypted)
        print("Saved encrypted data to des_cfb_encrypted.bin")
        
        # 6. Decrypt to verify
        cipher = DES.new(key, DES.MODE_CFB, iv=iv)
        decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)
        
        with open('des_cfb_decrypted.txt', 'wb') as f:
            f.write(decrypted)
        print("Saved decrypted data to des_cfb_decrypted.txt")
        
        # 7. Compare with OpenSSL
        print("Comparing with OpenSSL implementation...")
        with open('temp_plaintext.txt', 'wb') as f:
            f.write(plaintext)
            
        subprocess.run([
            'openssl', 'enc', '-des-cfb',
            '-in', 'temp_plaintext.txt',
            '-out', 'openssl_encrypted.bin',
            '-K', key.hex(),
            '-iv', iv.hex(),
            '-nopad'
        ], check=True)
        
        print("\nTask 4 completed successfully!")
        print("Generated files:")
        print(f"- {os.path.join(os.getcwd(), 'des_cfb_encrypted.bin')}")
        print(f"- {os.path.join(os.getcwd(), 'des_cfb_decrypted.txt')}")
        print(f"- {os.path.join(os.getcwd(), 'openssl_encrypted.bin')}")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Install pycryptodome: python3 -m pip install pycryptodome")
        print("2. Install OpenSSL: brew install openssl (Mac) or sudo apt install openssl (Linux)")
        print("3. Verify text file exists at ../../the_clockmaker_of_rothenburg.txt")

if __name__ == "__main__":
    run_des_cfb()