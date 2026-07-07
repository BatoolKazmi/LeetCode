class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        res, resLen = [-1, -1], float("inf")
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                left_char = s[l]
                window[left_char] -= 1
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""