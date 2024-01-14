from collections import Counter
def makeEqual(words):
    s=''
    if len(words)==1:
        return True
    s =''.join(words)
    c=Counter(s)
    for i in c.values():
        if i % len(words)!=0:
            return False
    return True

words = ["abc","aabc","bc"]
print(makeEqual(words))
