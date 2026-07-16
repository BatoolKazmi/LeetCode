class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxRes = 0
        hashmap = {}

        for i in arr:
            hashmap[i] = 1 + hashmap.get(i, 0)
        
        for num, count in hashmap.items():
            if num == count:
                maxRes = max(maxRes, num)
        return maxRes if maxRes != 0 else -1