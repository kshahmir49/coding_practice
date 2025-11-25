def myAtoi(self, s):
        s = s.strip()
        if s=="":
            return 0
        if s[0]!="-" and s[0]!="+" and not s[0].isdigit():
            return 0
        else:
            num = 0
            sign = 1
            start = 0
            if s[0]=="-":
                sign = -1
                start = 1
            if s[0]=="+":
                sign = 1
                start = 1
            for i in range(start,len(s)):
                if not s[i].isdigit():
                    break
                else:
                    num = num*10 + int(s[i])
            num = num * sign
            if num>(2**31)-1:
                return (2**31) - 1
            if num<(-2**31):
                return -2**31
            return num