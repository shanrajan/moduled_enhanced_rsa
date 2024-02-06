# decryption.py
from Crypto.Util.number import long_to_bytes

def decrypt(n, e, encrypted):
    return long_to_bytes(pow(encrypted, e, n)).decode()

if __name__ == "__main__":
    encrypted = int(input("Enter the Encrypted Message: "))
    # Input the private key (n, d)
    key_n, key_e = map(int, input("Enter the public key: ").split(','))

    decrypted = decrypt(key_n, key_e, encrypted)
    print(f"Decrypted Message: {decrypted}")
