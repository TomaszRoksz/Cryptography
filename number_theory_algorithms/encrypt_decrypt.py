def Euklides(a, b):
    x_a, y_a, x_b, y_b = 1, 0, 0, 1
    
    while a*b != 0:
        if a>=b:
            c=a//b
            a=a%b
            x_a = x_a - x_b * c
            y_a = y_a - y_b * c
        else:
            c = b // a
            b = b % a
            x_b = x_b - x_a * c
            y_b = y_b - y_a * c
            
    if a>0:
        x=x_a
        y=y_a
    else:
        x=x_b
        y=y_b  
        
    return x, y


def find_GCD(a, b):     

    x, y= Euklides(a, b)
    GCD=x*a+y*b
    
    return GCD

    
def calculate_a(A, Mi, Ni, M):
    
    a=0
    for i in range(len(A)):
        a+=A[i]*Mi[i]*Ni[i]
       
    return int(a%M)    


def find_a(A, B):
            
    #2
    M=1
    for i in range(len(B)):
        M*=B[i]
                   
    Mi=[M]*len(B)               
    for i in range(len(B)):
        Mi[i]=Mi[i]/B[i]
               
    #3
    Ni=[0]*len(B)
    for i in range(len(B)):
        Ni[i], trash=Euklides(Mi[i], B[i])
        if Ni[i]==0:
            return "Brak rozwiązania!!!"
            
    a=calculate_a(A, Mi, Ni, M)

    for z in range(len(A)):
        if A[z]!=a%B[z]:
            
            return "Brak rozwiązania!!!"
        
    return int(a)

def cipher(A, B):
    
    code=[]
    for i in range(len(A)):
        code.append(B%A[i])
        
    return code
        
        


command=input()

if command=="szyfruj":

    A=input().split()
    B=input()

    A= [int(x) for x in A]
    B= int(B)

    a=cipher(A, B)

    result=""
    for i in range(len(a)):
        result+=str(a[i])+" "
        
    print(result[:-1])
    
else:
    B=input().split()
    A=input().split()

    A= [int(x) for x in A]
    B= [int(x) for x in B]
    
    a=find_a(A, B)

    print(a)
    




