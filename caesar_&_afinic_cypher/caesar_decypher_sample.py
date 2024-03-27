def text_input():
    text=input()
    key=input()
            
    return text, key
    
def chars_ascii(text):
        
    ascii_numbers=[]
    for i in range(len(text)):
        ascii_numbers.append(ord(text[i]))
                             
    return ascii_numbers
                

def get_alphabet():
    alphabet=[]
    for i in range(65,123):
        if i<91 or i>96:
            alphabet.append(chr(i))
    return alphabet

def cipher(ascii_numbers, shift):
    alphabet=get_alphabet()
    
    text=""
    for i in range(len(ascii_numbers)):
        
        if ascii_numbers[i]>64 and ascii_numbers[i]<91:
            text+=alphabet[(ascii_numbers[i]-65-shift)%52]

            
        elif ascii_numbers[i]>96 and ascii_numbers[i]<123:
            text+=alphabet[(ascii_numbers[i]-71-shift)%52]
        else: text+=chr((ascii_numbers[i]))
                
    return text

def print_text(text):
    for i in range(0,len(text)):
        print("Klucz: "+str(i+1)+" | "+"Tekst: "+text[i])
   
    return 0

def cesear_analisys(ascii_numbers):
    codes=[]
    for i in range(1,53):
        codes.append(cipher(ascii_numbers, i))
        
    return codes

def decipher(codes, key):
    key=key.strip()
    import re
    for el in codes:
        if re.search(key, el):
            print(el)
            print(codes.index(el)+1)
            
        
        

        
       
        
            
    
                
            
            

    
text, key=text_input()

ascii_numbers=chars_ascii(text)

codes=cesear_analisys(ascii_numbers)

result=decipher(codes, key)
