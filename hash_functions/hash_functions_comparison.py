def hash_text(text, algorithm):
    hash_function = getattr(hashlib, algorithm)()
    hash_function.update(text.encode('utf-8'))

    return hash_function.hexdigest()


def generate_random_string(L):
    import random
    import string

    random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(L))

    return random_string


def check_for_collisions(string1, string2):

    if string1==string2:
        collisions=1
    else:
        collisions=0
   
    return collisions

    

import hashlib
import time

functions=["md5", "sha256", "sha1", "sha3_224", "blake2s"]
string_lengths=[1, 10, 100, 1000, 10000]

for string_length in string_lengths:
    random_string=generate_random_string(string_length)
    random_string2=generate_random_string(string_length)

    print("String Length: "+str(len(random_string)))

    for function in functions:
        
        hashed_functions=[]
        start_time = time.time()
        for i in range(1000):
            hash_text(random_string, function)
        end_time=time.time()
        collisions=check_for_collisions(random_string, random_string2)

        print(function+" - Time = ", "{:.4f}".format(end_time-start_time, 4), "seconds, Collisions = ", collisions)

    print("\n")
        
