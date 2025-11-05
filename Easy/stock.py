prices = [7,1,5,3,6,4]

def maxProfit(prices):
    p1,p2 = 0,0
    mp = 0
    while p2<len(prices):
        if prices[p1] < prices[p2]:
            mp = max(mp, prices[p2]-prices[p1])
        else:
            p1 = p2
        p2+=1
    return mp

print(maxProfit(prices))