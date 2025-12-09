class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        result = []

        for index, num in enumerate(numbers):
            rem = target - num
            if rem in num_dict :
                result = [num_dict.get(rem), index + 1]
                return result
            else:
                num_dict[num] = index + 1
        
        return result