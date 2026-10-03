#codesoft python programming
#Task3:Password Generator
import random
import string
print("========================")
print("PASSWORD GENERATOR")
print("=========================")
try:
    length=int(input("Enter password length:"))
    if length<=0:
        print("password length must br grater than 0:")
        exit()
except ValueError:
    print("please enter a valid number:")
    exit()
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(length):
    password+=random.choice(characters)
random.choice(characters)
print("\nGenerated Password:",password)
