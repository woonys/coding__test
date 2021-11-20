from sys import stdin

V, E = map(int, stdin.readline().split())

Vroot = [i for i in range(V+1)] # 정점의 루트값을 저장하는 부모 리스트 => 0부터 V까지 값 저장해놓음
Elist = [] # 정점 & 간선 저장해놓는 리스트

for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key = lambda x: x[2])  # 간선 가중치(x[2]) 기준으로 Elist 정렬

def find(x): # 정점의 루트를 찾는 함수
    if x != Vroot[x]: # x값이 Vroot의 인덱스 x에 위치한 값과 다르면 
        Vroot[x] = find(Vroot[x]) # 재귀 돌린다 => 루트 찾을 떄까지!
    return Vroot[x]

answer = 0
 # Union 파트!
for s, e, w in Elist: # s: 정점 1, e: 정점 2, w: 간선 가중치(weight)
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot: # 연결된 두 정점의 루트가 다르다면
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot # sRoot 인덱스만큼에 해당하는 루트값은 eRoot
        else:
            Vroot[eRoot] = sRoot # 반대
        answer += w
print(answer)