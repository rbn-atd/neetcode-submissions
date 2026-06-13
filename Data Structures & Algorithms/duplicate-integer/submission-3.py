class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tally = {}
        for i in nums:
            if i in tally:
                return True
            else:
                tally[i] = 1
        return False
        