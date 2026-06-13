class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ts={}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in ts:
                return [ts[difference], i]
            ts[nums[i]] = i

