def text_input():
    text=input()
    key=input()
              
    return text, key

def chars_to_ascii(text):
        
    ascii_numbers=[]*len(text)
    for i in range(len(text)):
        ascii_numbers.append(ord(text[i]))
        
    return ascii_numbers 

def key_chars_to_ascii(key):
        
    ascii_numbers=[]
    for i in range(len(key)):
        number=ord(key[i])
        
        if number>64 and number<91:
            ascii_numbers.append(number-65)

        elif number>96 and number<123:
            ascii_numbers.append(number-97)
            
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
      

    
text, key=text_input()      
text_ascii_numbers=chars_to_ascii(text)
key_ascii_numbers=key_chars_to_ascii(key)

text=decipher(text_ascii_numbers, key_ascii_numbers)
print(text)