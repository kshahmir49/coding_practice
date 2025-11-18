inp = [8,9,9,9]
if inp[-1] != 9:
    inp = inp[:-1] + [inp[-1]+1]
else:
    res = 1
    inp[-1] = 0
    for i in range(len(inp)-2,-1,-1):
        if inp[i] != 9:
            inp[i] = inp[i] + res
            res = 0
            break
        else:
            inp[i] = 0
    if res==1:
        inp.insert(0,res)
print(inp)