

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

   
            
            

a=input()
a, b=a.split()
a, b=int(a), int(b)

x, y= Euklides(a, b)
GCD=x*a+y*b

result=str(x)+' '+str(y)+' '+str(GCD)
print(result)
