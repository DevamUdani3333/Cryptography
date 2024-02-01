import hashlib

pt=input("Enter Your Data :-")

result=hashlib.sha512(pt.encode())

print(result.hexdigest())

print(result)
