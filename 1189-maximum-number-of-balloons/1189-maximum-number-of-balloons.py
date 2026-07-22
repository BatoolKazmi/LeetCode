class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        want = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        have = {}

        for c in text:
            have[c] = 1 + have.get(c, 0)
        
        res = float("inf")
        for c, need in want.items():
            if c not in have:
                return 0
            possible = have[c] // need
            res = min(res, possible)
        return res