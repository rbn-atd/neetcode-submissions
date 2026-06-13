class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences={}
        for i in range(len(nums)):
            difference=target-nums[i]
            #store dict of differences to find matching pair for each num
            #{difference, index}
            #find difference and then check if it is already in dict
            #if in dict return index of difference and current index
            if difference in differences:
                return [differences[difference], i]
            differences[nums[i]] = i