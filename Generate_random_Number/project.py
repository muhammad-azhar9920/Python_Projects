import random
import string

pass_len = 12
password = ""
pass_data = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Logic 1
# list comprehension (function for i in range(n))
password = "".join([random.choice(pass_data) for i in range(pass_len)])

# Logic 2
# for i in range(pass_len):
#     password += random.choice(pass_data)

print("Your random Password =",password) 
