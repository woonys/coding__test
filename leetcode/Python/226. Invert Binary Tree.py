# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
How to solve: my own solution - dfs를 쓴다. 이때 주의점: 파이썬에서는 swap을 한 줄로 처리할 수 있음! 자바는 어떻게 이걸 해결해야 하지..? 무조건 temp 소환해야 될듯.
시간복잡도: O(N) - N는 Leaf 노드 제외한 노드 수 -> 이 수 만큼 dfs 함수 호출된다.
공간복잡도: O(1) -> 실질적으로 위치만 바꾸는 거라 공간이 늘어나지 않음.

Runtime: 40 ms, faster than 60.41% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14 MB, less than 11.24% of Python3 online submissions for Invert Binary Tree.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root:
                root.left, root.right = root.right, root.left # 파이썬에서 가능한 작업!
                dfs(root.left)
                dfs(root.right)
            return root
        return dfs(root)