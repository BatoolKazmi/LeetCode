class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0 
        
        for c in nums:
            hashmap[c] = 1 + hashmap.get(c,0)
        for c, i in hashmap.items():
            if i >= 2:
                res += i * (i -1) // 2
        return res
