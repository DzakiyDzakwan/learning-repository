class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_dict = {}
        major_count = len(nums) / 2

        for num in nums :
            num_dict[num] = 1 + num_dict.get(num, 0)

        major_number = max(num_dict, key=num_dict.get)

        return major_number
        
# Alternate Solutiion
class Solution(object):
    def majorityElement(self, nums):
        sol = None
        cnt = 0
        for i in nums:
            if cnt == 0:
                sol = i
            cnt += (1 if i == sol else -1)
        return sol