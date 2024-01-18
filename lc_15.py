def climbStairs(n):
    if n<=2:
        return n
    
    a, b, x = 1, 2, 0
    
    for i in range(2,n):
        x = a + b
        a = b
        b = x
    return x
n=3
print(climbStairs(n))      