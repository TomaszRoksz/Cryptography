def hash_text(text, algorithm):
    hash_function = getattr(hashlib, algorithm)()
    hash_function.update(text.encode('utf-8'))

    return hash_function.hexdigest()


def generate_random_string(L):
    import random
    import string

    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(L))

    return random_string


    

import hashlib
import time

functions=["md5", "sha256", "sha1", "sha3_224", "blake2s"]
string_lengths=[1, 10, 100, 1000, 10000]

for string_length in string_lengths:
    random_string=generate_random_string(string_length)
    print("String Length: "+str(len(random_string)))

    for function in functions:
        

        start_time = time.time()
        for i in range(10000):
            hash_text(random_string, function)
        end_time=time.time()

        print(function+" - Time = ", "{:.4f}".format(end_time-start_time, 4))

    print("\n")
        
