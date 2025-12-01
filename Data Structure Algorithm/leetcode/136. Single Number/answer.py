class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        num_dict = {}

        for num in nums:
            num_dict[num] = 1 + num_dict.get(num, 0)

        result = min(num_dict, key=num_dict.get)
        return result
        