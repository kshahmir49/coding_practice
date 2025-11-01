nums = [2,7,11,15]
target = 26

def two_sum2(nums):
    i = 0
    j = len(nums)-1
    for _ in range(len(nums)):
        if nums[i] + nums[j] == target:
            return [i+1,j+1]
        elif nums[i] + nums[j] > target:
            j = j-1
        else:
            i = i+1
print(two_sum2(nums))