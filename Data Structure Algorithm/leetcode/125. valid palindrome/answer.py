class Solution(object):
    def isAlphanum(self, char):
        return (
            ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9")
        )
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        head = 0
        tail = len(s) - 1

        while head < tail:
            while head < tail and not self.isAlphanum(s[head]):
                head += 1
            while tail > head and not self.isAlphanum(s[tail]):
                tail -= 1

            if s[head].lower() != s[tail].lower():
                return False

            head += 1
            tail -= 1
        
        return True
        