res = 0

def depth_first(tree):
    global res
    if not tree:
        return -1
        l = depth_first(tree.left)
        r = depth_first(tree.right)
        res = max(res, l+r+2)
        return 1 + max(l, r)

def dia_bt(tree):
    depth_first(tree)
    return res