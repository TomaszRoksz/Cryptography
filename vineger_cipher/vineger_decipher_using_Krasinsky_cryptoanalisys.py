#Calculating possible key length

def text_input():
    text=input()
              
    return text

def clear_text(text):
    clear_text=""
    
    for i in range(len(text)):
        number=ord(text[i])
        if number>64 and number<91:
            clear_text+=(text[i])
        elif number>96 and number<123:
            clear_text+=(text[i].upper())
        
    return clear_text 

def sequences_search(text):
    patterns=dict()
    distances=[]
    
    for i in range(len(text)-2):
        pattern=text[i:i+3]
        if pattern not in patterns:
            patterns[pattern]=0
        
        for j in range(len(text)-2):
        
            if pattern==text[j:j+3] and i != j:
                distances.append(abs(i-j))
            
    return distances

def calculate_dividers(number):
    dividers_list=[]
    
    if number<3: return number
    
  
    for i in range(2,int(number/2)+1):
        if number%i==0:
            dividers_list.append(i)
    if number<26:        
        dividers_list.append(number)
        
    return dividers_list



def find_key_length(distances):
    keys=[]
    
    for el in distances:
            keys.append(calculate_dividers(el))  
            
    return keys

def find_key_length_occurancies(keys):#finds most probable key length from all possible keys
    occurancies=[0]*100
        
    for row in keys:
        for el in row:
            if el<100:
                occurancies[el]+=1
                                           
    return occurancies

def find_most_common_key_length(key_length_occurancies):
    max_occurance=0
    
    for i in range(1,26):
        if max_occurance<key_length_occurancies[i]:
            max_occurance=key_length_occurancies[i]
            key=i
    key_length_occurancies[key]=0
            
    return key, key_length_occurancies


#Calculating possible letters occurancy for a single shift:


def get_alphabet():
    alphabet=[]
    
    for i in range(65,91):
        alphabet.append(chr(i))
        
    return alphabet

def text_to_list(text):
    text_list=[0]*26
    alphabet=get_alphabet()
    
    for i in range(len(text)):
        if text[i] in alphabet:
            text_list[alphabet.index(text[i].upper())]+=1
            
    return text_list

def matching_letters(letters_occurancy):
    most_occurancies=sorted(letters_occurancy)[-6]
    least_occurancies=sorted(letters_occurancy)[5]
    
    most_frequent=["E", "T", "A", "O", "I", "N"]
    least_frequent=["V", "K", "J", "X", "Q", "Z"]

    frequency=0
    
    if most_occurancies>0:
        for el in most_frequent:
            if letters_occurancy[ord(el)-65] >= most_occurancies:
                frequency+=1
                
    if least_occurancies>0:
        for el in least_frequent:
            if letters_occurancy[ord(el)-65] <= least_occurancies:
                frequency+=1
                
    return frequency


#Function checking all combinations in a concrete key lengths


def frequency_analisys(divided_text):
    
    frequency=[]
      
    for j in range(26):
        temp=""
        
        for k in range(len(divided_text)):
            temp+=chr((ord(divided_text[k])-65-j)%26+65)
            
        letters_occurancy=text_to_list(temp)
                    
        frequency.append((j, matching_letters(letters_occurancy)))
        
    temp=[]    
    temp=sorted(frequency, key=lambda x: x[1], reverse=True)
    frequency=[]
    max_value=temp[0][1]
    
    for i in range(len(temp)):
        #print(temp[i][1], max_value)
        if temp[i][1]>max_value-2:
            frequency.append(temp[i][0]) 
        else:
            break
        
    #print(len(frequency), frequency)
            
    return frequency
    
def divide_text(text, key_length):
    divided_text=[""]*key_length
    
    for i in range(len(text)):
        divided_text[i%key_length]+=text[i]
        
    return divided_text
    
    
def key_length_analisys(key_length, text):
    frequency=[]
    divided_text=divide_text(text, key_length)

    match=0
    
    for i in range(key_length):
        frequency.append(frequency_analisys(divided_text[i]))    
    
    return frequency    
    
def every_key_length(key_length_occurancies, text):
    frequency=[]
    key, key_length_occurancies=find_most_common_key_length(key_length_occurancies)
    
    frequency=(key_length_analisys(key, text))
        
    return frequency, key_length_occurancies
        

#CHECKING SUGGESTED KEYS WITH DICTIONARY


def text_without_special_characters(text):
    clear_text=""
    
    for i in range(len(text)):
        number=ord(text[i])
        
        if number>64 and number<91:
            clear_text+=(text[i])
            
        elif number==32:
            clear_text+=(text[i])
            
        elif number>96 and number<123:
            clear_text+=(text[i].upper())
        
    return clear_text 
    
def generate_combinations(list_of_lists):
    result = []
    
    from itertools import product    
    
    all_combinations = product(*list_of_lists)
    
    for combination in all_combinations:
        result.append(list(combination))
    
    return result
    
def chars_to_ascii(text):
    ascii_numbers=[]*len(text)
    
    for i in range(len(text)):
        ascii_numbers.append(ord(text[i]))
        
    return ascii_numbers 

def decipher(ascii_numbers, key):
    text=""
    letter_no=0
    
    for i in range(len(ascii_numbers)):
        j=letter_no%len(key)
        
        if ascii_numbers[i]>64 and ascii_numbers[i]<91:
            text+=chr((ascii_numbers[i]-65-key[j])%26+65)
            letter_no+=1
            
        elif ascii_numbers[i]>96 and ascii_numbers[i]<123:
            text+=chr((ascii_numbers[i]-97-key[j])%26+97)
            letter_no+=1
            
        else: text+=chr((ascii_numbers[i]))
            
    return text

def print_key(shift):
    key=""
    
    for i in range(len(shift)):
        key+=chr(shift[i]+97)
        
    print(key)
    
      
    
def decipher_handler(original_text, text, shift):
    
    import requests
    r = requests.get("https://stepik.org/media/attachments/lesson/668860/dictionary.txt")
    dictionary=r.text.split()
    #print(shift)
    
    text_ascii_numbers=chars_to_ascii(text)
    
    if len(text)>99:
        for i in range(len(shift)):
            #print(shift[i])
            text=decipher(text_ascii_numbers[:50], shift[i])
            splitted_text=text.split()
            if dictionary_check(splitted_text[:3], dictionary, 0):
                text=decipher(text_ascii_numbers[:100], shift[i])
                splitted_text=text.split()
                if dictionary_check(splitted_text, dictionary, 5):
                    print(decipher(chars_to_ascii(original_text), shift[i]))
                    print_key(shift[i])
                    return True
                
    else:
            text=decipher(text_ascii_numbers, shift[i])
            if dictionary_check(text, dictionary, 3):
                print(decipher(chars_to_ascii(original_text), shift[i]))
                print_key(shift[i])
                return True
        
    return False
   

def dictionary_check(textt, dictionary, compliant_letters_number):
    import bisect
    correct_words=0
    
    #textt=text_cipher.split()
    
    for i in range(len(textt)):
        x=bisect.bisect_left(dictionary,textt[i])
        
        if x != len(dictionary) and dictionary[x] == textt[i]:           
            correct_words+=1
            
    if correct_words>compliant_letters_number:
        return True
    else:
        return False
    

#__MAIN__


#Calculating possible key length:   

    
text=text_input()      
cleared_text=clear_text(text)
distances=sequences_search(cleared_text)


#Calculating possible letters occurancy:


all_key_lengths=find_key_length(distances)

key_length_occurancies=find_key_length_occurancies(all_key_lengths)


#CHECKING SUGGESTED KEYS WITH DICTIONARY


decipher_text=text_without_special_characters(text)

for x in range(4):
    
    frequency, key_length_occurancies=every_key_length(key_length_occurancies, cleared_text)
    
    #if len(frequency) != 6:
        #break
    
    proposed_keys=(generate_combinations(frequency))
    
    if decipher_handler(text, decipher_text, proposed_keys):
        break



