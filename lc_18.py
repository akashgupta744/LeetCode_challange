def rearrangeArray(nums):
    l1, l2=[], []
    for i in range(len(nums)):
        if nums[i] > 0:
            l1.append(nums[i])
        else:
            l2.append(nums[i])
    nums=[]    
    for j in range(len(l1)):
        nums.append(l1[j])
        nums.append(l2[j])
    return nums    

nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
        