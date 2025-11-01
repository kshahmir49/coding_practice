s = input("Enter value for s: ")
t = input("Enter value for t: ")

def anagram(s,t):
    if len(s) != len(t):
        return False
    else: 
        s_count = {}
        t_count = {}
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i],0)
            t_count[t[i]] = 1 + t_count.get(t[i],0)
        for j in s_count:
            if s_count[j] != t_count[j]:
                return False
        return True
    
print(anagram(s,t))