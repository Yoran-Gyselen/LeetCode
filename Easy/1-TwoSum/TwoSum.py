from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        for i, num in enumerate(nums):
            lookup_num = target - num
            lookup_num_index = nums.index(lookup_num) if lookup_num in nums else None 
            if lookup_num in nums and i != lookup_num_index:
                solution.append(i)
                solution.append(lookup_num_index)
                return solution