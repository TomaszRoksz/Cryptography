def text_input():
    text=[]
    
    while True:
        try:
            line = input()
            text.append(line)
        except EOFError:
            break
    
    shift=text[-1]
    text=text[:-1]
            
    return text, int(shift)
    
def chars_ascii(text):
        
    if len(text)>1:
        ascii_numbers=[[] for _ in range(len(text))]
        for i in range(len(text)):
            for j in range(len(text[i])):
                ascii_numbers[i].append(ord(text[i][j]))
                
    else: 
        ascii_numbers=[]*len(text)
        text=str(text)
        for j in range(len(text)):
            ascii_numbers.append(ord(text[j]))
    return ascii_numbers

def list_of_list(ascii_numbers):
    for i in range(len(ascii_numbers)):
        if isinstance(ascii_numbers[i], list):
            return True
    return False

def get_alphabet():
    alphabet=[]
    for i in range(65,123):
        if i<91 or i>96:
            alphabet.append(chr(i))
    return alphabet

def cipher(ascii_numbers, shift):
    alphabet=get_alphabet()
    
    if list_of_list(ascii_numbers)==True:
        text=[""]*len(ascii_numbers)
    
        for i in range(len(ascii_numbers)):

            for j in range(len(ascii_numbers[i])):
            
                    if ascii_numbers[i][j]>64 and ascii_numbers[i][j]<91:
                        text[i]+=alphabet[(ascii_numbers[i][j]-65-shift)%52]
            
                    elif ascii_numbers[i][j]>96 and ascii_numbers[i][j]<123:
                        text[i]+=alphabet[(ascii_numbers[i][j]-71-shift)%52]
                    else: text[i]+=chr((ascii_numbers[i][j]))
    else:
        text=""
        for i in range(len(ascii_numbers)):
        
            if ascii_numbers[i]>64 and ascii_numbers[i]<91:
                text+=alphabet[(ascii_numbers[i]-65-shift)%52]
            
            elif ascii_numbers[i]>96 and ascii_numbers[i]<123:
                text+=alphabet[(ascii_numbers[i]-71-shift)%52]
            else: text+=chr((ascii_numbers[i]))
                
    return text

def print_text(text):
    if type(text)==str:
        print(text[2:-2])
    else:
        for el in text:
            print(el)        
    return 0
        
       
        
            
    
                
            
            

    
text, shift=text_input()
    
ascii_numbers=chars_ascii(text)


text=cipher(ascii_numbers, shift)
print_text(text)

