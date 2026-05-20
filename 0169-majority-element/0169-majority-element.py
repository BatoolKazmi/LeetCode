class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maxCount = 0
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if maxCount < count[n]:
                res = n
                maxCount = count[n]
        
        return res