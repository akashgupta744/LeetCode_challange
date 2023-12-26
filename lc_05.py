def numRollsToTarget(n, k, target):
    mod=10**9+7
    ans=0
    l=0
    while l*k<=(target-n):
        res=(target-n)-(l*k)
        ans=(ans+((-1)**l)*comb(n,l)*comb(res+n-1,n-1))%mod
        l+=1
    return ans    
ModuleNotFoundError(1,3,6)