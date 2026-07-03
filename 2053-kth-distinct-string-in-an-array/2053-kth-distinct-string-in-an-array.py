class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        distinct = 0

        for item in arr:
            hashmap[item] = hashmap.get(item, 0) + 1

        for item in hashmap:
            if hashmap[item] == 1:
                distinct += 1
            if distinct == k:
                return item
        return ""