# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 값 계속 저장하는 용도
    val = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #오른쪽 -> 자기 자신 -> 왼쪽:
        #bstToGst(right) -> root.val 값 바꾸고 -> bstToGst(left) 
        #추상화 개념 잘 써야! 들어가면 나머지는 알아서 해준다는 믿음.
        if root:
            self.bstToGst(root.right)
            root.val = self.val = root.val + self.val
            self.bstToGst(root.left)
        return root
        
        