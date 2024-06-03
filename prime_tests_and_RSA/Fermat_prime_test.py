def generate_random_numbers(n, k_times, s):
    import random
    random.seed(s)
    random_numbers = [random.randint(2,n-1) for i in range(k)]
    
    return random_numbers


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


def power(a, b, n):
    result=1
    
    a=a%n
    
    if a==0:
        return 0
        
    while b > 0:
    
        if ((b&1)==1):
            result=(result*a)%n
        
        b=b>>1
        a=(a*a)%n
    
    return result

def fermat_prime_test(n, k, s):
    if n==2: return 1
    
    random_numbers=generate_random_numbers(n, k, s)
    
    for i in range(k):
        a=random_numbers[i]
        #print(a)

        GCD=find_GCD(a, n)
    
        if GCD>1:
            return 0
        else:
            a=power(a, n-1, n)
            
            GCD=find_GCD(a, n)
            
            if GCD>1:
                return 0
        
    return 1


input=input()

n, k, s=input.split()
n, k, s = int(n), int(k), int(s)


if fermat_prime_test(n, k ,s):
    print("Liczba prawdopodobnie pierwsza")
else: print("Liczba złożona")
