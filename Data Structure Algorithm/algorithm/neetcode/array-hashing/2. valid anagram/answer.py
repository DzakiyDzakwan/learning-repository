class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        for letter in s:
            if letter in t:
                t.remove(letter)
            else:
                print(t)
                return False

        if t:
            return False
        else:
            return True
        
# Built in Method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
# Using Hashmap
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS = {}
        counterT = {}

        for i in range(len(s)) :
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)
        
        for c in counterS:
            if counterS[c] != counterT.get(c, 0):
                return False
            
        return True