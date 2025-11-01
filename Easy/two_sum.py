nums = [2,11,7,15]
target = 9

## Not efficient
# def two_sum(nums):
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

def two_sum(nums):
    k = {}
    for i in range(len(nums)):
        if k.get(target - nums[i]) != None:
            return [k.get(target - nums[i]), i]
        else:
            k[nums[i]] = i
    return k
print(two_sum(nums))