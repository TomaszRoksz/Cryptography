def text_input():
    text=input()
    key=input()
              
    return text, key

def generate_random(n, k):

    import random

    random.seed(k)

    bytes_string=str(random.randbytes(n))
    
    return (bytes_string[2:-1])

def chars_to_bin(text):
        
    ascii_numbers=[]*len(text)
    flag=0
    
    for i in range(len(text)):
        
        if text[i]=='\\' and flag==0:
            
            if text[i+1]=='x':
                ascii_numbers.append(int(text[i+2:i+4], 16))
                flag=3
                
            #elif text[i+1]=='a':
                #ascii_numbers.append(7)
                #flag=1
            
            #elif text[i+1]=='b':
                #ascii_numbers.append(8)
                #flag=1
                
            elif text[i+1]=='t':
                ascii_numbers.append(9)
                flag=1
                
            elif text[i+1]=='n':
                ascii_numbers.append(10)
                flag=1
                
            elif text[i+1]=='v':
                ascii_numbers.append(11)
                flag=1
                
            #elif text[i+1]=='f':
                #ascii_numbers.append(12)
                #flag=1
                
            elif text[i+1]=='r':
                ascii_numbers.append(13)
                flag=1
                
            elif text[i+1]=='"':
                ascii_numbers.append(34)
                flag=1
                
            elif text[i+1]=='\'':
                ascii_numbers.append(39)
                flag=1
                
            elif text[i+1]=='\\':
                ascii_numbers.append(92)
                flag=1
                
                
            else: ascii_numbers.append(int(format(ord(text[i]), 'b'), 2))
                
        elif flag != 0:
            flag-=1
                
        else:
            ascii_numbers.append(int(format(ord(text[i]), 'b'), 2))
        
    return ascii_numbers 


def XOR(text1_bin, text2_bin):
    
    if len(text2_bin)<len(text1_bin):
        text2_bin,text1_bin=text1_bin,text2_bin
        
    
    for i in range(len(text1_bin)):
        text1_bin[i]=text1_bin[i] ^ text2_bin[i]
            
    return text1_bin 

def switch_ascii(code):
    switch = {
        9: r'\t',
        10: r'\n',
        11: r'\v',
        #12: r'\f',
        13: r'\r',
        34: r'"',
        39: r'\'',
        #92: r'\\',
    }   
    return switch[code]


def cipher(numbers):
    
    text=r""
    
    for i in range(len(numbers)):
        
        if numbers[i]<32 or numbers[i]>126:
            if numbers[i]<12 and numbers[i]>8:
                text+=switch_ascii(numbers[i])
            elif numbers[i]==13 or numbers[i]==34 or numbers[i]==39:
                text+=switch_ascii(numbers[i])
            elif numbers[i]==92:
                text+=r'//'+r'//'
            else:             
                hex_number=format((numbers[i]), 'x')
            
                if len(hex_number)<2:
                    text+="\\x0"+str(hex_number)
                
                else: text+="\\x"+str(hex_number)
        
        else: text+=chr((numbers[i]))
                
    return text
      
    
text1, seed=text_input() 

text1_bin=chars_to_bin(text1)
key=generate_random(len(text1_bin), int(seed))
text2_bin=chars_to_bin(key)


numbers_xor=XOR(text1_bin, text2_bin)
result=cipher(numbers_xor)

print(result)
