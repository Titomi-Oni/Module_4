import string
import random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

all_chars = lower + upper + digits

length = 8

password_list = [random.choice(all_chars) for _ in range(length)]
random.shuffle(password_list)

password = ''.join(password_list)
print (password)