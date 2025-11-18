im = [[1,2,3], [4,5,6],[7,8,9]]

l = 0
r = len(im) - 1
while l<r:
    for i in range(r-l):
        top = l
        bottom = r
        # saving tl
        temp = im[top][l+i]
        # swapping tl with bl
        im[top][l+i] = im[bottom-i][l]
        # swapping bl with br
        im[bottom-i][l] = im[bottom][r-i]
        # swapping br with tr
        im[bottom][r-i] = im[top+i][r]
        # swapping tl with temp
        im[top+i][r] = temp
    l += 1
    r -= 1
print(im)