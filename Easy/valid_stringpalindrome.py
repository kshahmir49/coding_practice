def isPalindrome(self, s):
        s = s.lower()
        s = "".join([a for a in s if a.isalnum()])
        if s == s[::-1]:
            return True
        return False