# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []

        q = collections.deque([root])

        while q:
            qLen = len(q)
            rightSide = None

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node.val
                    q.append(node.left)
                    q.append(node.right)

            if rightSide is not None:
                res.append(rightSide)

        return res