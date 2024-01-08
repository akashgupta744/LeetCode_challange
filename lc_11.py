l=[2,4,5,9,11,123]
def isprime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
print(list(filter(isprime,l)))