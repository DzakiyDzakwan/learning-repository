class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        first_string = strs.pop(0)

        # Loop substring firs string letter
        for i in range(len(first_string)):
            is_match = True
            
            # Loop substring in string from array
            for string in strs:
                # if index the same with string length then break the loop
                if i >= len(string):
                    is_match = False
                    break

                if first_string[i] != string[i]:
                    is_match = False
            
            # if the letter didn't match then break the loop
            if is_match:
                result += first_string[i]
            else :
                break

        return result
    

# Best Solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Sort the list
        strs.sort()
        
        # Get the first string and the last string from array
        first, last = strs[0], strs[-1]

        # set index
        i = 0

        while i< len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
