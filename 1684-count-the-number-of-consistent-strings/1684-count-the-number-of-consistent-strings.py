class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        hashmap = {}
        res = 0

        for c in allowed:
            hashmap[c] = 1 + hashmap.get(c, 0)
        
        for w in words:
            good = True
            for j in w:
                if j not in hashmap:
                    good = False
            
            if good:
                res += 1
        return res
