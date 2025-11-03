import random

import string



print("Welcome to the BBC Password Generator ")



# Ask user for length

length = int(input("Enter desired password length: "))



# Characters to use

characters = string.ascii_letters + string.digits + string.punctuation



# Generate password

password = ""

for i in range(length):

    password += random.choice(characters)



print("\n Your generated password is:", password)