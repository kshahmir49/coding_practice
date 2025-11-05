# n = 3
# import math

# alls = 0
# if n%2 == 0 :
#     alls=2
#     for i in range(1, n//2):
#         alls += math.factorial(n-i)/(math.factorial(n-2*i)*math.factorial(i))
        
# else:
#     alls=1
#     for i in range(1, n//2 + 1):
#         alls += math.factorial(n-i)/(math.factorial(n-2*i)*math.factorial(i))
# print(int(alls))

def climb_stairs(n):
    l = 1
    l_1 = 1
    steps = 0
    for _ in range(n-1):
        temp = l_1
        l_1 = l_1 + l
        l = temp
    return l_1
print(climb_stairs(5))