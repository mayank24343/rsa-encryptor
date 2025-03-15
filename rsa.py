import random

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def find_nums():
    while True:
        p = random.choice(primes)
        while True:
            q = random.choice(primes)
            if q != p:
                break
        n = p*q 
        if n >= 128:
            return p,q,n

def gcd(a,b):
    if a%b == 0:
        return b 
    else:
        return gcd(b,a%b)
    
def create_keys():
    p,q,n = find_nums()
    phi = (p-1)*(q-1)

    e = find_e(phi)
    d = find_dnew(phi,e)
    pbk = [e,n]
    pvk = [d,n]

    return pbk,pvk,phi,p,q

def find_e(phi):
    for i in range(2,phi):
        if gcd(i,phi) == 1:
            return i 
        
def find_d(phi,e):
    d = 1
    while True:
        if (e*d) % phi == 1:
            return d 
        d+=1 

def find_dnew(phi,e):
    k = 1
    while True:
        d = (k*phi+1)/e 
        if d == int(d):
            return int(d)
        k+=1

def encrypt(plaintext,e,n):
    encrypted = ''
    for i in plaintext:
        m = ord(i)
        x = (m**e)%n 
        encrypted+=chr(x)

    return encrypted

def decrypt(encrypted,d,n):
    decrypted = ''
    for i in encrypted:
        m = ord(i)
        x = (m**d)%n 
        decrypted+=chr(x)

    return decrypted


