# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        odd_q, even_q = [root], []
        rtList = [[root.val]]
        while odd_q and odd_q[-1]:
            rtList.append([])
            while odd_q:
                focus = odd_q.pop()
                if focus.right:
                    even_q.append(focus.right)
                    rtList[-1].append(focus.right.val)
                if focus.left:
                    even_q.append(focus.left)
                    rtList[-1].append(focus.left.val)
            rtList.append([])
            while even_q and even_q[-1]:
                focus = even_q.pop()
                if focus.left:
                    odd_q.append(focus.left)
                    rtList[-1].append(focus.left.val)
                if focus.right:
                    odd_q.append(focus.right)
                    rtList[-1].append(focus.right.val)
        while not rtList[-1]:
            rtList.pop()
        return rtList
