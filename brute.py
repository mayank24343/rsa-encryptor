import rsa
import requests
import new 

def breakrsa(pbk,t):
    e,n = pbk
    '''for i in primes:
        for j in primes:
            if i!=j and i*j == n:
                p,q = i,j
                print(i,j)
    
    for i in primes:
        if n/i == n//i:
            print(i,n//i)
            p,q = i,n//i'''
    
    x = 2
    while True:
        if isprime(x):
            if n%x == 0:
                p,q = x,n//x
                break
        x+=1

    phi = (p-1)*(q-1)
    d = 1
    while True:
        if (e*d)%phi == 1:
            break
        d+=1
  
    return rsa.decrypt(t,d,n)

def isprime(n):
    
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False 
        
    return True

def breakmatrix(text):
    storage = []
    for i in range(1,8):
        for j in range(1,8):
            decrypted = new.decrypt(text,[i,j])
            l = decrypted.split()
            k = l[0]
            if isword(k):
                storage.append(decrypted)

    return storage 

def isword(word):
    data = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
    data = data.json()

    if len(data)==1:
        if data[0]['phonetics']:
            return True 
        
    return False
