alpha = "abcdefghijklmnopqrstuvwxyz"

def ceaser_decrypt(text, key):
    size = len(text)
    plaintext = ""

    for i in range(size):
        char = text[i]
        if char.isalpha():
            index = alpha.find(char.lower())
            newindex = (index + key)
            newchar = alpha[newindex]

            if char.isupper():
                newchar = newchar.upper()

            plaintext += newchar
        else:
            plaintext += char
    return plaintext
ciphertext = input("Enter the ciphertext to decrypt: ")

print("Brute Force Decryption: ")
for key in range():
    decrypted_text = ceaser_decrypt(ciphertext,key)
    print(f"Key{key}: {decrypted_text}")