from collections import defaultdict
def findWinners(matches):
    lost = defaultdict(int)
   
        
    for m in matches:
        lost[m[0]] += 0
        lost[m[1]] += 1
    
    
    zero = sorted([k for k, l in lost.items() if l == 0])
    ones = sorted([k for k, l in lost.items() if l == 1])
    print(zero)
    return [zero, ones]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(findWinners(matches))