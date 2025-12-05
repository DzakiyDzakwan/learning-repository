class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        head = 0
        tail = len(s) - 1
        palindromes = {}

        while head <= tail:
            curr_head = head
            curr_tail = tail

            while curr_tail >= head:
                if s[curr_tail] == s[curr_head]:
                    temp_head = curr_head
                    temp_tail = curr_tail
                    palindrome = ""

                    while temp_tail >= curr_head:
                        if s[temp_head] != s[temp_tail]:
                            palindrome = ""
                            break

                        palindrome += s[temp_head]
                        temp_tail -= 1
                        temp_head += 1
                    
                    palindromes[palindrome] = len(palindrome)
                    
                curr_tail -= 1
            head += 1

        return max(palindromes, key=palindromes.get)
    
# Alternate Solution
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        longest_palindrome_indices = (0, 0)
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand_around_center(i, i)
            len1 = r1 - l1 + 1

            l2, r2 = expand_around_center(i, i + 1)
            len2 = r2 - l2 + 1
            
            if len1 > len2:
                current_start, current_end = l1, r1
                current_len = len1
            else:
                current_start, current_end = l2, r2
                current_len = len2
            
            if current_len > longest_palindrome_indices[1] - longest_palindrome_indices[0] + 1:
                longest_palindrome_indices = (current_start, current_end)

        start, end = longest_palindrome_indices
        return s[start:end+1]