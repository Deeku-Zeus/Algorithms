import io
import os

def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def printPrimes(n,m):
    res=[]
    for i in range(n,m+1):
        print("i i i="+str(i))
        f=True
        for j in range(2,i):
            f=True
            print("j="+str(j))
            if i%j == 0:
                f=False
                break
        if f :res.append(i)
    return res
op=0
while(True):
    try:
        op = int(input("Press 1 for checking if number is Prime.\nPress 2 for printing primes in a range [n m].\n"))
        if op != 1 and op != 2:
            os.system("cls")
            print("Choose Again !!")
            continue
        break
    except:
        os.system("cls")
        print("Choose Again !!")
while(True):
    if op == 1 :
        try:
            n=int(input("Enter a number: "))
            res = isPrime(n)
            if res == True:
                print("{} is a prime number.".format(n))
            else:
                print("{} is not a prime number.".format(n))
            break
        except:
            os.system("cls")
            print("Choose Again !!")
    if op == 2:
        try:
            r=(input("Enter range n m :")).split(" ",1)
            n=int(r[0])
            m=int(r[1])
            res = printPrimes(n,m)
            if not res:
                print("{}-{} doesn't have any prime numbers.".format(n,m))
            else:
                print("Primes:\n")
                print(*res,sep="\n")
            break
        except:
            os.system("cls")
            print("Choose Again !!")