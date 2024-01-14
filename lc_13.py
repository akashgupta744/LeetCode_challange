from collections import Counter

def closeStrings(word1, word2):
    c1 = Counter(word1)
    c2 = Counter(word2)

    sortedword1 = sorted(c1.values())
    sortedword2 = sorted(c2.values())
    
    keys_match = set(c1.keys()) == set(c2.keys())
    
    return sortedword1 == sortedword2 and keys_match
word1, word2 = "cabbba", "aabbss"
print(closeStrings(word1, word2))