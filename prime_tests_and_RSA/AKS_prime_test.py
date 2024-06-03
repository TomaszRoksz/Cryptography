def strong(n): return n*strong(n-1) if n > 1 else 1


def calculate_newton_binomial(n, k):
    return strong(n)/(strong(k)*strong(n-k))

def AKS(n):
    import math
    if n%2==0: return 0
    
    for i in range(n-1):
        factor=math.comb(n, i)
        
        if i>0:
            if factor%n!=0:
                return 0
            
    return 1         
            
    

    
    
n=int(input())

if n==0 or n==1:
    print("Podałeś 0 lub 1!")
else:
    if AKS(n):
        print("Liczba pierwsza")
    else: print("Liczba złożona")
