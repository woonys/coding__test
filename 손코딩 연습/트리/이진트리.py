class Node: # 바이너리 트리 구성할 노드 클래스 생성
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def preorder(node):
        print(node.data, end="")
        if node.left != "" : preorder(node.left)
        if node.right != "": preorder(node.right)
        
    def inorder(node):
        if node.left != "": inorder(node.left)
        print(node.data, end="")
        if node.right != "": inorder(node.right)
    
    def postorder(node):
        if node.left != "": postorder(node.left)
        if node.right != "": postorder(node.right)
        print(node.data, end = "")