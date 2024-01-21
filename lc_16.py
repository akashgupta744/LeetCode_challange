def rob(nums):
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[0], nums[1])

    dp = [0] * n
    print(dp)
    dp[0] = nums[0]
    print(dp)
    dp[1] = max(nums[0], nums[1])
    print(dp)

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)

    return dp[n-1]
nums = [1,2,3,1]
print(rob(nums))
        

        

        