# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder/inorder가 비어있으면 종료
        if not preorder or not inorder:
            return None
        
        #예외 케이스: node가 하나만 있는 경우
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode()
        root.val = preorder[0]
        
        root_idx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root

        
        
        
        
        
#         if not preorder or not inorder:
#             return None
        
#         if len(preorder)== 1:
#             return TreeNode(preorder[0])
        
#         root = TreeNode()    
#         root.val = preorder[0]
        
#         root_idx = inorder.index(preorder[0])
        
        
#         root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
#         root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
#         return root

        
        
        
 
        
#         self.root.val = preorder[0]
#         if len(preorder) == 1:
#             return self.root
#         root_idx_inorder = inorder.index(self.root.val) #inorder에서 root 위치
#         left_fin = inorder[root_idx_inorder-1]
#         left_fin_pre = preorder.index(left_fin)
        
#         #print(root_idx_inorder)
#         #if self.root:
#             # for root.right
#             # for root.left
#         self.root.left = self.buildTree(preorder[1:left_fin_pre+1], inorder[:root_idx_inorder])
#         self.root.right = self.buildTree(preorder[left_fin_pre+1:], inorder[root_idx_inorder+1:])
#         return self.root