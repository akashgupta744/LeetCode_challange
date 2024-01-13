def minSteps(s, t):
        cs = [0]*26
        ct = [0]*26
        
        for i in s:
            cs[ord(i) - ord('a')] += 1
        for i in t:
            ct[ord(i) - ord('a')] += 1
        steps = 0
        for j in range(26):
            steps += abs(cs[j] - ct[j])
        
        return steps // 2
s,t = 'aba', 'bab'
s,t = 'leetcode', 'practice'
# s,t = 'anagram', 'margana'
print(minSteps(s,t))
