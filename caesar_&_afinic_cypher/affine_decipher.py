def text_input():
    text=[]
    
    while True:
        try:
            line = input()
            text.append(line)
        except EOFError:
            break
    
    key=text[-1]
    text=text[:-1]
            
    key=list(map(int, key.split()))
            
    return text, key

def is_key_correct(key):
    a=abs(key[0])
    if a==0: return False
    elif a==1: return True
    elif a<26:
        for i in range(2,a+1):
            if 26%i==0 and a%i==0:
                return False
        return True
    elif a>26:
        for i in range(2,26):
            if 26%i==0 and a%i==0:
                return False
        return True
    return False
        
    
def chars_ascii(text):
        
    if len(text)>1:
        ascii_numbers=[[] for _ in range(len(text))]
        for i in range(len(text)):
            for j in range(len(text[i])):
                ascii_numbers[i].append(ord(text[i][j]))
                
    else: 
        ascii_numbers=[]*len(text)
        text=str(text)
        text=text[2:-2]
        for j in range(len(text)):
            ascii_numbers.append(ord(text[j]))
    return ascii_numbers

def list_of_list(ascii_numbers):
    for i in range(len(ascii_numbers)):
        if isinstance(ascii_numbers[i], list):
            return True
    return False
                

def decipher(ascii_numbers, key):
    a_opposite=find_opposite_element(key[0])
    b=key[1]
    
    if list_of_list(ascii_numbers)==True:
        text=[""]*len(ascii_numbers)
    
        for i in range(len(ascii_numbers)):

            for j in range(len(ascii_numbers[i])):
            
                    if ascii_numbers[i][j]>64 and ascii_numbers[i][j]<91:
                        text[i]+=chr((a_opposite*(ascii_numbers[i][j]-65-b))%26+65)
            
                    elif ascii_numbers[i][j]>96 and ascii_numbers[i][j]<123:
                        text[i]+=chr((a_opposite*(ascii_numbers[i][j]-97-b))%26+97)
                    else: text[i]+=chr((ascii_numbers[i][j]))
    else:
        text=""
        for i in range(len(ascii_numbers)):
        
            if ascii_numbers[i]>64 and ascii_numbers[i]<91:
                text+=chr((a_opposite*(ascii_numbers[i]-65-b))%26+65)
            
            elif ascii_numbers[i]>96 and ascii_numbers[i]<123:
                text+=chr((a_opposite*(ascii_numbers[i]-97-b))%26+97)
            else: text+=chr((ascii_numbers[i]))
                
    return text

def extended_euklides(a, b):
    # Base Case 
    if a == 0 : 
        return b,0,1
             
    gcd,x1,y1 = extended_euklides(b%a, a) 
     
    # Update x and y using results of recursive 
    # call 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y 

def find_opposite_element(a):
    b = 26
    g, x, y = extended_euklides(a, b) 
    
    return x%26

def print_text(text, a_opposite , b_opposite):
    if type(text)==list:
        for i in range(len(text)):
            print(text[i])
    else:
        print(text)
        
    print(a_opposite, b_opposite)
       
    return 0

       
       
            

    
text, key=text_input()

if is_key_correct(key): 

    ascii_numbers=chars_ascii(text)
    
    a_opposite=find_opposite_element(key[0])    

    text=decipher(ascii_numbers, key)
           
    print_text(text, a_opposite, key[1])
    
else: print("BŁĄD")





