def replaceElements(self, arr):
    max_el = -1
    for i in range(len(arr)-1,-1,-1):
        temp = max(max_el,arr[i])
        arr[i] = max_el
        max_el = temp
    return arr