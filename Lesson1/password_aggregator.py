from random import seed
from random import randint
import string

# alpha_list = ["a", "b", "c", "d", "e", "f"]
alpha_list = string.punctuation + string.ascii_letters + string.digits
password_result = ""
password_len = 20

for _ in range(password_len):
    random_int = randint(0, len(alpha_list) - 1)
    random_letter = alpha_list[random_int]
    password_result += random_letter

print(password_result)
