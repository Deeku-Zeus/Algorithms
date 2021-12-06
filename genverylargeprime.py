import io
import math as m
from random import randrange, getrandbits,randint

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length,minnum,maxnum):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    #p = getrandbits(length)
    #ensure number is greater than min number
    p=0
    tc=0
    while p < minnum or p > maxnum:
        tc+=1
        # generate random bits
        p = getrandbits(length)
        print("random bit : {}".format(p))
        if tc > 1000:
            print("having trouble generating a randome number !! Try again.")
            exit()
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=1024,minnum=0,maxnum=0):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length,minnum,maxnum)
    return p
numdigs = int(input("Enter number of digits :"))
#numbits = int(input("Enter number of bits :"))
mindig = 10**(numdigs-1)
minbit = m.ceil(m.log2(mindig))+1 if m.floor(m.log2(mindig)) == m.ceil(m.log2(mindig)) else m.ceil(m.log2(mindig))
maxdig = (10**(numdigs))-1
maxbit = m.ceil(m.log2(maxdig))+1 if m.floor(m.log2(maxdig)) == m.ceil(m.log2(maxdig)) else m.ceil(m.log2(maxdig))
numbits=randint(minbit,maxbit)
primenum = generate_prime_number(numbits,mindig,maxdig)
print("Prime : {}".format(primenum))
#print("log10 of prime {}".format(m.log10(primenum)))
#print("len of prime {}".format(m.ceil(m.log10(primenum))))
#print("{} digit numbers range from {} - {}.\nCan be represented from {} - {} bits".format(numdigs,mindig,maxdig,minbit,maxbit))