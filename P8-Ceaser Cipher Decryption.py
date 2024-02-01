alpha = "abcdefghijklmnopqrstuvwxyz"

ciphertext = input("Enter your data: ")
key = int(input("Enter your key: "))

size = len(ciphertext)
plaintext = ""

for i in range(size):
    char = ciphertext[i]
    if char.isalpha():
        index = alpha.find(char.lower()) #Convert to lowercase for case insentive encryption
        newindex = (index - key) %26
        newchar = alpha[newindex]

        #Preserve the original case (uppercaser or lowercase) of the character
        if char.isupper():
            newchar = newchar.upper()
        
        plaintext += newchar
    else:
        #If it is not a letter, just add it as it is without changing anything
        plaintext += char
print("Ciphertext,",plaintext)