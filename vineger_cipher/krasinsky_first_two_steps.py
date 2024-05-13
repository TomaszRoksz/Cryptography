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

def print_key_lengths(keys):
    
    temp=[]
    string=""
    
    for row in keys:
        for el in row:
            if el<17:
                temp.append(el)
                
    temp.sort()
    occurancies=[0]*17
    
    for i in range(len(temp)):
        occurancies[temp[i]]+=1
    
                
    for i in range(len(occurancies)):
        if occurancies[i]>1:
            string+=str(i)+" "
        
    print(string)
          

    
text=text_input()      
text=clear_text(text)
distances=sequences_search(text)
keys=find_key_length(distances)

print_key_lengths(keys)

