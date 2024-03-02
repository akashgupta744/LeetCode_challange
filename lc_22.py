def sortedSquares(nums):
    return sorted([i**2 for i in nums])
    
nums = [-4,-1,0,3,10]
print(sortedSquares(nums))