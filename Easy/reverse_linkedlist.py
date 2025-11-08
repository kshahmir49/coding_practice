def reverseLL(ll):
    prev = None
    curr = ll

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

