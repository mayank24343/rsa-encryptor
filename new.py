import random 

def create_shift(m,n):
    i = random.randint(1,m-1)
    j = random.randint(1,n-1)
    return [i,j]

def encrypt(text):
    matrix = [list('abcdefgh'),list('ijklmnop'),list('qrstuvwx'),list('yzABCDEF'),
              list('GHIJKLMN'),list('OPQRSTUV'),list('WXYZ1234'),list('567890 .')]
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            d[matrix[i][j]] = [i,j]
    
    encrypted = ''
    step = create_shift(len(matrix),len(matrix[0]))
    for i in text:
        try:
            encrypted += find_encrypted(matrix,d[i],step)
        except:
            encrypted += i 

    return encrypted,step
    

matrix = [list('abcdefgh'),list('ijklmnop'),list('qrstuvwx'),list('yzABCDEF'),
              list('GHIJKLMN'),list('OPQRSTUV'),list('WXYZ1234'),list('567890 .')]

def find_encrypted(matrix,start,steps):
    i,j = start
    m = len(matrix)
    n =  len(matrix[0])
    i += steps[0]
    j += steps[1]
    if i >= m:
        i = i - m 
    if j >= n:
        j = j - n 

    return matrix[i][j]

def decrypt(text,step):
    matrix = [list('abcdefgh'),list('ijklmnop'),list('qrstuvwx'),list('yzABCDEF'),
              list('GHIJKLMN'),list('OPQRSTUV'),list('WXYZ1234'),list('567890 .')]
    d = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            d[matrix[i][j]] = [i,j]

    m = len(matrix)
    n =  len(matrix[0])

    decrypted = ''
    for k in text:
        try:
            i,j = d[k]
            i -= step[0]
            j -= step[1]
            if i < 0:
                i += m
            if j < 0:
                j += n 
            decrypted+=matrix[i][j]
        except:
            decrypted+=k

    return decrypted
