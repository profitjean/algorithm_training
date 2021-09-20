import sys

def isPrime(x) :
    if x == 1 :
        return False
    for i in range(2, int(x**(0.5))+1) :
        if x%i == 0 :
            return False
    return True

n = int(sys.stdin.readline())
while(n!=0) :
    for k in range(3, n-2, 2) :
        if isPrime(k) :
            a = k
            b = n-a
            if isPrime(b) :
                Goldbach = True
                break
            else :
                Goldbach = False
        else :
            Goldbach = False
    if Goldbach :
        print('{} = {} + {}'.format(n, a, b))
    else :
        print("Goldbach's conjecture is wrong.")
    n = int(sys.stdin.readline())