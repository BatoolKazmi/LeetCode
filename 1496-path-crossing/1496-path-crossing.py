class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hashmap = {}
        horizontal, vertical = 0, 0 
        hashmap[(vertical, horizontal)] = hashmap.get((vertical, horizontal), 0) + 1

        for i in range(len(path)):
            if path[i] == "N":
                vertical += 1
            elif path[i] == "S":
                vertical -= 1
            elif path[i] == "E":
                horizontal += 1
            elif path[i] == "W":
                horizontal -= 1
            
            if (vertical, horizontal) in hashmap:
                return True
            hashmap[(vertical, horizontal)] = hashmap.get((vertical, horizontal), 0) + 1
        return False