def invertTree(self, root):
    if root == None:
        return None
    temp = root.right
    root.right = root.left
    root.left = temp
    invertTree(root.right)
    invertTree(root.left)
    return root