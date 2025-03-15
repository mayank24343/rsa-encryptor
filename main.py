import rsa as encryption
import brute
import new 

def menu():
    print("ENCRYPT")
    print("Would you like to:\nA: Encrypt Text Using RSA\nB: Decrypt RSA Encyrpted Text\nC: Encrypt Text Using Matrix\nD: Decrypt Matrix Encrypted Text")
    choice = input("Enter Choice[A/B/C/D]:")
    if choice == 'A':
        text = input("Enter Text:")
        pbk,pvk,phi,p,q = encryption.create_keys()
        e,n = pbk
        encrypted =  encryption.encrypt(text,e,n)
        print("Encrypted Text is:",encrypted)
        print("Public Key is:",pbk)
    elif choice == 'B':
        text = input("Enter Text:")
        key = eval(input("Enter Public Key [e,n]:"))
        decrypted = brute.breakrsa(key,text)
        print("Decrypted Text is:",decrypted)
    elif choice == 'C':
        text = input("Enter Text:")
        encrypted,shift = new.encrypt(text)
        print("Encrypted Text is:",encrypted)
        #print("Shift as [down,right] is",shift)
    elif choice == 'D':
        text = input("Enter Text:")
        print("Decryption Will Take Some Time :(")
        storage = brute.breakmatrix(text)
        print("Possible Decryptions Could Be:")
        for i in storage:
            print(i)
    else:
        print('Invalid Option')

menu()

