class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: 
            return -1

        mid = len(nums)//2
        if len(nums)>=mid:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return self.search(nums[:mid], target)
            else:
                result = self.search(nums[mid+1:], target)  
                return -1 if result == -1 else mid + 1 + result  
            