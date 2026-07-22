class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        hashmap = {}
        for c in nums:
            hashmap[c] = 1 + hashmap.get(c, 0)

        for c, have in hashmap.items():
            if have % 2 != 0:
                return False
        return True

