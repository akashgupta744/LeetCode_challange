from collections import Counter

def maxFrequencyElements(nums):
    count = Counter(nums)
    maxFreq = max(count.values())
    ans = 0
    
    for val in count.values():
        if val==maxFreq:
            ans+=val
            
    return ans
print(maxFrequencyElements([1,2,3,4,5]))