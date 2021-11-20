# from sys import stdin
# from collections import deque
#
# n = int(stdin.readline())
# graph = dict()
# for i in range(n):
#     parent, child1, child2 = map(str, stdin.readline().split())
#     graph[parent] = [child1, child2]
#
#
# def pre_trav(graph, start_node):
#     visited = ["."] # 이미 방문한 노드 넣기
#     queue = deque()
#     queue.append(start_node)
#
#     while queue:
#         node = queue.popleft()
#
#         if node not in visited:
#             visited.append(node)
#
#             queue.extend(graph[node])
#     return "".join(visited[1:])
#
# print(pre_trav(graph, next(iter(graph))))


# from sys import stdin


# class Node:
#     def __init__(self, item, left, right):
#         self.item = item  # 부모 노드 => key로 저장
#         self.left = left  # 왼쪽 자식 노드
#         self.right = right  # 오른쪽 자식 노드


# def preorder(node):  # 전위 순회: <자기 자신 => 왼쪽 노드 => 오른쪽 노드>
#     print(node.item, end="")  # 전위 순회에서는 if 문 통과하면서 재귀 돌리기 전에 먼저 자기부터 print
#     if node.left != '.':  # 점이 찍혀있다는 건 자식 노드가 없다는 뜻이므로 if 문을 지나치는 자체가 종료 조건!
#         preorder(tree[node.left])  # 재귀로 왼쪽 자식 노드에 대한 전위 순회 돌려
#     if node.right != '.':
#         preorder(tree[node.right])


# def inorder(node):  # 중위 순회: <왼쪽 자식 노드 => 자기 노드 => 오른쪽 자식 노드> 순서이니 아래 재귀 돌릴 때도 이에 맞게 순서!
#     if node.left != ".":
#         inorder(tree[node.left])  # 중위
#     print(node.item, end="")
#     if node.right != ".":
#         inorder(tree[node.right])


# def postorder(node):  # 후위 순회: <왼쪽 노드 => 오른쪽 노드 => 자기 자신>
#     if node.left != '.':
#         postorder(tree[node.left])
#     if node.right != '.':
#         postorder(tree[node.right])
#     print(node.item, end='')


# if __name__ == "__main__":

#     n = int(stdin.readline())
#     tree = {}  # 부모/자식 노드 담을 곳 => 빈 딕셔너리 생성

#     for _ in range(n):
#         node, left, right = map(str, stdin.readline().split())
#         tree[node] = Node(item=node, left=left, right=right)  # tree[node] => key로 부모 노드를 저장하고 value로 노드 클래스를 저장!

#     preorder(tree['A'])
#     print()
#     inorder(tree['A'])
#     print()
#     postorder(tree['A'])


# 다시 보고 짜보기!


from sys import stdin


class Node:
    def __init__(self, item, left, right) -> None:
        self.item = item # 부모 노드 저장
        self.left = left # 왼쪽 자식 노드
        self.right = right # 오른쪽 자식 노드


def preorder(node): # 전위 순회: 자기 자신 방문 -> 왼쪽 자식 -> 오른쪽 자식
    print(node.item, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
    
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end="")


if __name__ == "__main__":
    n = int(stdin.readline())
    tree = {}
    for i in range(n):
        node, left, right = map(str, stdin.readline().split())
        tree[node] = Node(item = node, left = left, right = right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])