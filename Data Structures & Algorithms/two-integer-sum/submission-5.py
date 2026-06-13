class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tally={}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in tally:
                return [tally[difference], i]
            tally[nums[i]] = i

