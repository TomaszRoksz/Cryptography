def text_input():
    text=input()
    key=input()
              
    return text, key

def chars_to_bin(text):
        
    ascii_numbers=[]*len(text)
    flag=0
    
    for i in range(len(text)):
        
        if text[i]=='\\' and flag==0:
            
            if text[i+1]=="x":
                ascii_numbers.append(int(text[i+2:i+4], 16))
                flag=3
                
            elif text[i+1]=="n":
                ascii_numbers.append(10)
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


def cipher(numbers):
    
    text=""
    
    for i in range(len(numbers)):
        
        if numbers[i]<33 or numbers[i]>126:
            hex_number=format((numbers[i]), 'x')
            
            if len(hex_number)<2:
                text+="\\x0"+str(hex_number)
                
            else: text+="\\x"+str(hex_number)
        
        else: text+=chr((numbers[i]))
                
    return text
      
    
text1, text2=text_input()      

text1_bin=chars_to_bin(text1)
text2_bin=chars_to_bin(text2)

numbers_xor=XOR(text1_bin, text2_bin)
result=cipher(numbers_xor)


print(result)



