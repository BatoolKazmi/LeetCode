class Solution:
    def compress(self, chars: List[str]) -> int:
        w = 0 # write pointer
        r = 0 # read pointer
        n = len(chars)

        while r < n:
            chars[w] = chars[r]
            w += 1
            j = r + 1

            while j < n and chars[j] == chars[r]:
                j += 1
            count = j - r

            if count > 1:
                for number in str(count):
                    chars[w] = number
                    w += 1
            
            r = j

        return w