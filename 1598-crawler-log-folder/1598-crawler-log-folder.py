class Solution:
    def minOperations(self, logs: List[str]) -> int:
        directory = 0

        for n in range(len(logs)):
            if logs[n] == "./":
                continue
            elif logs[n] == "../":
                directory -= 1 if directory > 0 else 0
            else:
                directory += 1
        
        return directory