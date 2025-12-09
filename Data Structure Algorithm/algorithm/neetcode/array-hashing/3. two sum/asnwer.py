class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        number_dict = {}
        result = []

        for i in range(len(nums)):
            remain = target - nums[i]

            if remain in number_dict:
                result.append(number_dict[remain])
                result.append(i)
                return result
            
            number_dict[nums[i]] = i

        return result