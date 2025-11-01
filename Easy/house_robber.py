nums = [1,2,3,1]

def house_robber(nums):
    c1,c2 = 0,0
    for i in nums:
        temp = max(c2, i+c1)
        c1 = c2
        c2 = temp
    return c2

print(house_robber(nums))