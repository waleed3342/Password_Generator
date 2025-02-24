import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("Welcome to Password Generator.")

qty_letters = int(input("How many letters would you like in your password.  "))
qty_numbers = int(input("How many numbers would you like in your password.  "))
qty_symbols = int(input("How many symbols would you like in your password.  "))

password_list = []  

# Adding letters according to user choice
for pass_word in range(qty_letters):
    password_list.append(random.choice(letters))

# Adding numbers according to user choice
for pass_word in range(qty_numbers):
    password_list.append(random.choice(numbers))

# Adding symbols according to user choice
for pass_word in range(qty_symbols):
    password_list.append(random.choice(symbols))

# Joining the password list into a single string or also shufling because i want it to be randomised
random.shuffle(password_list)
password = ''.join(password_list)

print("Your password is: ", password)