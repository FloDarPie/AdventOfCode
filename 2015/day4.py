input = "bgvyzdsv"

import hashlib

def find_lowest_number(secret_key):
    number = 0
    while True:
        input_string = secret_key + str(number)
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()
        
        if md5_hash.startswith('000000'):
            return number
        number += 1


print(find_lowest_number(input))