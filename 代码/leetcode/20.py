class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        a=deque([])
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                deque.append(a,s[i])
            elif s[i]==")":
                if a and a[-1]=="(":
                    deque.pop(a)
                else:
                    return False
            elif s[i]=="]":
                if a and a[-1]=="[":
                    deque.pop(a)
                else:
                    return False
            elif s[i]=="}":
                if a and a[-1]=="{":
                    deque.pop(a)
                else:
                    return False
        if a:
            return False
        else:
            return True

