nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_sum(nums):
    sum = nums[0]
    current_sum = 0
    for i in range(len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        sum = max(sum,current_sum)
    return sum

print(max_sum(nums))