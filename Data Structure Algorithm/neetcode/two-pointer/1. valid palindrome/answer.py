class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += char.lower()

        return new_string == new_string[::-1]
    
# Alternate Solution
class Solution:
    def isAlnum(self, char) :
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )

    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s)-1

        while head < tail:
            while head < tail and not self.isAlnum(s[head]):
                head += 1
            while tail > head and not self.isAlnum(s[tail]):
                tail -= 1

            if s[head].lower() != s[tail].lower():
                return False
            
            head += 1
            tail -= 1
        return True