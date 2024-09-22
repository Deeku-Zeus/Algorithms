import io
import math as m

n = -1000
for i in range(1,n+1):
    b=m.ceil(m.log2(i))+1 if m.floor(m.log2(i)) == m.ceil(m.log2(i)) else m.ceil(m.log2(i))
    d=m.ceil(m.log10(i))+1 if m.floor(m.log10(i)) == m.ceil(m.log10(i)) else m.ceil(m.log10(i))
    print("{} can be represented in {} bits and digits is {}".format(i,b,d))

dig = int(input("Enter number of digits : "))
mindig = 10**(dig-1)
minbit = m.ceil(m.log2(mindig))+1 if m.floor(m.log2(mindig)) == m.ceil(m.log2(mindig)) else m.ceil(m.log2(mindig))
maxdig = (10**(dig+1))-1
maxbit = m.ceil(m.log2(maxdig))+1 if m.floor(m.log2(maxdig)) == m.ceil(m.log2(maxdig)) else m.ceil(m.log2(maxdig))
print("{} digit numbers range from {} - {}.\nCan be represented from {} - {} bits".format(dig,mindig,maxdig,minbit,maxbit))
