class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2): return False

        countS1, countS2 = [0] * 26, [0] * 26

        # checking the count of s1 & the first few count for s2 (in len(s1))
        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1
        
        # Checking how many matches there is initially 
        match = 0
        for i in range(26):
            match += (1 if countS1[i] == countS2[i] else 0)

        # Checking the whole s2 with sliding window checkin if s1 is found in s2
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: return True

            index = ord(s2[r]) - ord('a')
            countS2[index] += 1
            if countS2[index] == countS1[index]:
                match += 1
            elif countS1[index] + 1 == countS2[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            countS2[index] -= 1
            if countS2[index] == countS1[index]:
                match += 1
            elif countS1[index] - 1 == countS2[index]:
                match -= 1
            l += 1
        return match == 26
