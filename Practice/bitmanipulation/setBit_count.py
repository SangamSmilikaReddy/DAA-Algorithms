def SetBit(n):
    sb=0
    while n>0:
        n=n&(n-1)
        sb+=1
    return sb

N=8
print(SetBit(N))