'''
how to solve: 답안 참고
시간복잡도: O(V): V는 노드 개수 -> 노드 수만큼 함수 호출
공간복잡도: O(1)
'''

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root and root.val < val:
            return self.searchBST(root.right, val)
        elif root and root.val > val:
            return self.searchBST(root.left, val)
        return root