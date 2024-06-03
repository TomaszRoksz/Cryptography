def generate_random_numbers(n, k_times, s):
    import random
    random.seed(s)
    random_numbers = [random.randint(2,n-2) for i in range(k)]
    
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


def power_of_critical_number(n):
    temp=0
    i=2
    j=2
    
    while i*i<=n:
        while temp<n:
            temp=i**j
            j+=1
        
        if temp==n:
            return 1
        else:
            i+=1
            j=2
            
    return 0


def calculate_m(n):
    m=n-1
    s=0
    
    while (m & 1)==0:
        m >>= 1
        s+=1
            
    return int(m), s

def prime_factors_bitwise(n):
    factors = []

    while (n & 1) == 0:
        factors.append(2)
        n >>= 1

    factor = 3
    max_factor = int(n**0.5) + 1
    while factor <= max_factor:
        while (n % factor) == 0:
            factors.append(factor)
            n //= factor
            max_factor = int(n**0.5) + 1
        factor += 2

    if n > 1:
        factors.append(n)

    return factors    
    

def rabin_miller_test(n, k, s):
          
    if (n & 1) ==0:
        return 0
    
    random_numbers=generate_random_numbers(n, k, s)
    
    m, k_power=calculate_m(n)
       
    for i in range(k):
        a=random_numbers[i]

        GCD=find_GCD(a, n)
    
        if GCD>1:
            return 0
        
        else:
            for j in range(k_power):
                temp=power(a, m*(2**j), n)
                
                if temp==1:
                    
                    if j==0:
                        return 1
                    else:
                        
                        if power(a, m*(2**(j-1)), n)==-1 or power(a, m*(2**(j-1)), n)==n-1:
                            return 1
                        else:
                            return 0
    return 0



#MAIN


input=input()

n, k, s=input.split()
n, k, s = int(n), int(k), int(s)

if rabin_miller_test(n, k ,s):
    print("Liczba jest prawdopodobnie pierwsza")
else: 
    factors=prime_factors_bitwise(n)
    factors_str = ' * '.join(map(str, factors))
    
    print("Liczba złożona:", factors_str)
