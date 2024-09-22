import random
import string

print(string.digits)
print(string.ascii_letters)
s = string.digits + string.ascii_letters
v = random.sample(s, 4)
print("".join(v))
