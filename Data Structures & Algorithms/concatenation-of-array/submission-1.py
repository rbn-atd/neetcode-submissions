class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        doubleArray=[0]*(2*n)
        for i in range(n):
            doubleArray[i] = nums[i]
            doubleArray[i+n] = nums[i]
        return doubleArray