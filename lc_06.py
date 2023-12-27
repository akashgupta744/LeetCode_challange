
def minCost(colors, neededTime):
    totalTime = 0
    i = 0
    j = 0

    while i < len(neededTime) and j < len(neededTime):
        currTotal = 0
        currMax = 0

        while j < len(neededTime) and colors[i] == colors[j]:
            currTotal += neededTime[j]
            currMax = max(currMax, neededTime[j])
            j += 1

        totalTime += currTotal - currMax
        i = j

    return totalTime


s='abaac'
neededTime=[1,2,3,4,5]
print(minCost(s,neededTime))