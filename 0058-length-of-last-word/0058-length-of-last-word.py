class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        res = 0

        for i in range(len(arr[len(arr) - 1])):
            res += 1
        return res
        