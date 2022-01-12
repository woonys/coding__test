# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ["#"]
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
                result.append(str(node.val))
            else:
                result.append("#")
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str -> 그래서 serialize에서 str로 넘겨줘야!
        :rtype: TreeNode
        """
        
        
    
        treelist = data.split(" ")
        if data == "# #":
            return None
        
        root = TreeNode(int(treelist[1]))
        queue = collections.deque([root])
        index = 2
        while queue:
            node = queue.popleft()
            if treelist[index] is not "#":
                print(treelist[index])
                node.left = TreeNode(int(treelist[index]))
                queue.append(node.left)
            index +=1
            
            if treelist[index] is not "#":
                node.right = TreeNode(int(treelist[index]))
                queue.append(node.right)
            index +=1
        return root
            
    

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))