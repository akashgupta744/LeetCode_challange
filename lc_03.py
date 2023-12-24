def minOper(s,b):
    count = 0
    print(len(s))
    for i in range(0,len(s),2):
        
        if s[i:i+2] != b :
            if s[i] != b[0]:
                count +=1
            if len(s[i:i+2]) == 2 and s[i+1] != b[1] :
                count +=1

        print(count,s[i:i+2])
    return count
s="101101111"
f = minOper(s,'01')
d= minOper(s,'10')
print(f,d)

        # or

def minOper(s, b):
        count = 0
        for i in range(len(s)):
            if s[i] != b[i % 2]:
                count += 1
        return count
s="101101111"
print(min(minOper(s, '01'), minOper(s, '10')))