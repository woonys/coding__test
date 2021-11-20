# 이진 검색 트리 구현하기

# from __future__ import annotations
# from typing import Any, Type
#
# class Node:
#     # 이진 검색 트리의 노드
#     def __init__(self, key: Any, value: Any, left: Node = None,
#                  right: Node = None): # key, value: 임의의 형(Any), left, right: 왼쪽/오른쪽 자식으로 참조(포인터)를 None으로 나타냄
#
#         """생성자(constructor)"""
#         self.key = key  # 키
#         self.value = value  # 값
#         self.left = left  # 왼쪽 자식 노드
#         self.right = right  # 오른쪽 자식 노드
#
#
# class BinarySearchTree:
#     """이진 검색 트리"""
#
#     def __init__(self):
#         """초기화"""
#
#         self.root = None # 루트를 나타냄.


# from sys import stdin, setrecursionlimit

# setrecursionlimit(10**9)
# preorder = [] # 문제에서는 프리오더가 주어지고 그에 대한 포스트오더를 구해야 하는 문제.

# # step 1: 프리오더 값 받아오기
# while True:
#     try:
#         preorder.append(int(stdin.readline()))
#     except:
#         break

# """
# 주어진 이진 검색 트리의 프리오더를 살펴보자.
# 1. 주어진 프리오더의 루트는 첫번째 요소.
# 2. 이후 주어진 프리오더를 탐색하다가 루트보다 커지는 첫번째 요소부터 루트의 오른쪽 트리.
# 3. 오른쪽 트리의 시작을 기준으로 나누면 한 개의 프리오더는 루트 / 왼쪽 트리 프리오더 / 오른쪽 트리 프리오더로 나눌 수 있음.
# """

# # step 2: postorder 알고리즘 짜기
# postorder = []
# def postorderset(preorder, left, right): # 후위 순회 알고리즘 짜기
#     # 종료 조건 선언
#     if left > right: # 왼쪽 자식 노드가 오른쪽 자식노드보다 크다면: 이는 postorder가 아니니까 종료
#         return
#     root = preorder[left] # 루트 값 설정
#     left_start = left + 1 #
#     right_end = right #
#     right_start = right + 1
#     for i in range(right - left + 1):
#         if i == 0:
#             continue
#         if preorder[left + i] > root:
#             right_start = i + left
#             break

#     left_end = right_start - 1
#     postorderset(preorder, left_start, left_end) # postorderset은 왼쪽 자식 노드 -> 오른쪽 자식 노드 -> 자기 노드 탐색이니 여기서 왼쪽 노드 탐색하고
#     postorderset(preorder, right_start, right_end) # 여기서 오른쪽 노드 탐색하고
#     postorder.append(root) # 여기서 자기자신 append하면 postorderset!

# postorderset(preorder, 0, len(preorder)-1)

# for i in postorder:
#     print(i)


from sys import stdin, setrecursionlimit

setrecursionlimit(10**9)

preorder = []
while True:
    try:
        preorder.append(int(stdin.readline()))
    except:
        break


postorder = []
def postorderset(preorder, left, right): #프리오더 리스트와 가장 왼쪽(루트값) 인덱스, 오른쪽 끝 인덱스를 받아온다
    # step 1: 종료 조건 설정! left보다 right가 작아지면 종료하도록
    if left > right:
        return
    root = preorder[left]
    # step 2: 프리오더 = 부모 루트 + 왼쪽 자식 프리오더 + 오른쪽 자식 프리오더로 쪼갈라진다. 어디까지 left 프리오더이고 어디까지 right 프리오더인지 찾아야.
    # 현재 우리가 알고 있는 건? left_start는 루트 다음이라는 것(left+1), 오른쪽 끝인 right_end는 right인 것.
    left_start = left + 1 # 왼쪽 자식 프리오더가 시작하는 지점 => 왼쪽 프리오더에서 루트 값 인덱스에 해당하겠지.
    right_start = right + 1 # right_start는 아직 선언되지 않았으니 하나 더미값으로 만들어준다 => right 안에 없는 값으로.
    # 현재 우리가 모르는 건 left_end와 right_start. 이 right_start는 현재 루트보다 큰 값이 나올때임.
    for i in range(right-left+1): #전체 다 돌린다.
        if i == 0:
            continue
        if preorder[left + i] > root:
            right_start = i + left
            break
    
    left_end = right_start - 1
    right_end = right
    
    postorderset(preorder, left_start, left_end)
    postorderset(preorder, right_start, right_end)
    postorder.append(root)


postorderset(preorder, 0, len(preorder)-1)
for i in postorder:
    print(i)