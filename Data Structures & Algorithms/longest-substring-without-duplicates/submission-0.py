class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l=0
        result=0

        for r in range(len(s)):
            #if u find the current char in the set then move the window by
            #removing the left most elements until the current char is no longer in the set
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r]) #add current char to set if it is not in charSet or, 
            #if it was removed during the window slide
            result = max(result, r-l+1)#keep track of the largest window size to date

        return result