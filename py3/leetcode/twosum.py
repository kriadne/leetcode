class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(len(nums)):
            for ii in range(i+1, len(nums)):
                if nums[i] + nums[ii] == target:
                    return[i,ii]