# encryption.py
from Crypto.Util.number import bytes_to_long

def encrypt(n, d, message):
    return pow(bytes_to_long(message.encode()), d, n)

if __name__ == "__main__":
    message = input("Enter the Text to Encrypt: ")

    # Input the private key (n, d)
    key_n, key_d = map(int, input("Enter the private key: ").split(','))

    encrypted = encrypt(key_n, key_d, message)
    print(f"Encrypted Message: {encrypted}")
