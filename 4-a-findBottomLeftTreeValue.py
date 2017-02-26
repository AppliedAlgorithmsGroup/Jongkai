# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue1, queue2 = [root], []
        while queue1:
            leftMost = queue1[0]
            while queue1:
                focus = queue1.pop(0)
                if focus.left:
                    queue2.append(focus.left)
                if focus.right:
                    queue2.append(focus.right)
            if not queue2:
                return leftMost.val
            queue1, queue2 = queue2, queue1

