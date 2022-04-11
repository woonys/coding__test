'''
path의 특징을 저장하는 경우
    - 각 정점에 숫자가 적혀있고 a부터 b까지 가는 경로를 구하는데 경로에 같은 숫자가 있으면 안된다.
그래프에서 사이클 탐색하는 경우
'''

traced = set() # 경로를 저장
visited = set() # 노드 방문 저장

# 사이클이 있는 경우 False 반환
def dfs(node):
    if node in traced: # 경로에 같은 노드 중복 -> 사이클 존재
        return False
    if node in visited: # 이미 방문한 노드
        return True
    
    traced.add(node)
    for w in graph[node]:
        if not dfs(w):
            return False
    
    traced.remove(node) # 탐색 종료 후 경로에서 노드 삭제
    visited.add(node) # 탐색 종료 후 방문 처리
    return True