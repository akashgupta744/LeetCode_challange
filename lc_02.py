# Two SUM
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
print(twoSum([3,2,3],6))

        #   or

def twoSum(nums, target):
    result=[[i,j] for i in range(len(nums)-1) for j in range(i+1,len(nums)) if nums[i] + nums[j] == target]
    return result[0]
print(twoSum([3,2,3],6))

        #   or

def twoSum(nums, target):
    i=0
    while i < len(nums):
        d=target-nums[i]
        if d in nums[i+1:]:
            j=nums.index(d,i+1)
            return[i,j]
        
        i+=1

print(twoSum([3,2,4],6))


