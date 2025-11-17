def isPalindrome(self, head):
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        l, r = 0, len(lst)-1
        while l<=r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True
