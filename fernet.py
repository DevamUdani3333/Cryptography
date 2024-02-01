# Fernet module is imported from the cryptography package 
from cryptography.fernet import Fernet 





# key is generated 
key = Fernet.generate_key() 

# value of key is assigned to a variable 
f = Fernet(key) 

# the plaintext is converted to ciphertext 
C = f.encrypt(b"My name is vivek") 

# display the ciphertext 
print(C) 

# decrypting the ciphertext 
P= f.decrypt(C) 

# display the plaintext 
print(P) 
