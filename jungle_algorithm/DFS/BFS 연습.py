graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
root_node = 1

#BFS: Queue 자료구조를 사용 => Q는 줄서기.

# 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에 들어있던 노드부터 방문.

# Queue는 FiFO: First in, First Out => 먼저 온 애가 먼저 나간다. 줄서기 개념.
# 파이썬에서 큐를 list 타입으로 사용할 때는 뒤에서 넣으니까 append()를 쓰고, 나갈 때는

def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)
    # print("Start_node is: ", start_node)
    # print("queue is: ", queue)
    while queue:
        node = queue.pop(0)
        # print('node is: ', node)
        # print("queue is now: ", queue)
        if node not in visit:
            # print(f"새로운 방문지입니다. {node}를 visit에 추가합니다.")
            visit.append(node)
            # print("visit is now: ", visit)
            # print("graph[node] is: ", graph[node])
            queue.extend(graph[node])
            # print("Queue is after: ", queue)


    return visit

#print(bfs(graph, 'A'))

def dfs(graph, start_node): #얘는 stack 개념
