class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0

        for n in nums:
            if maxCount == 0:
                res = n 
            maxCount += (1 if res == n else -1)

        return res