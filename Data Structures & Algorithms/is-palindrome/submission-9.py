class Solution:
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s)-1

        while head < tail:
            #2 while loops to move pointers past non alphanumeric chars
            while head < tail and not self.alphaNum(s[head]):
                head += 1
            while tail > head and not self.alphaNum(s[tail]):
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            #no else here cuz i need to increment these all the time
            head += 1
            tail -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))