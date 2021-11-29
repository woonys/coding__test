"""
find_path(start, last, V, tmp_dist):
여행을 start에서 시작했고,(start = 시작 도시)
현재까지 방문한 중간 경로의 마지막 도시는 last,(last = 중간 경로의 마지막 방문 도시)
방문한 도시의 집합은 V, (V= 방문한 도시의 집합)
중간 경로의 길이는 tmp_dist일 때, (tmp_dist = 중간 경로의 길이)

해당 중간 경로를 사용해서 여행을 마쳤을 때의 완성된 모든 경로의 길이 최솟값은?


완탐에서는 이 인자를 모두 사용했으나 DP에서는 가능한 인자를 줄이고,
실제로 같은 인자에 대한 호출이 여러 번 일어나는지 확인해야!

문제를 푸는 데 필요한 핵심 인사이트 세 가지!

1. 구체적인 경로는 중요하지 않다.
방문한 도시의 집합을 비트 마스킹으로 구현만 할 줄 알면 오케이.
중요한 것은 여행 시작 도시와 현재 중간 경로에서의 마지막 방문 도시, 그리고 각 도시의 방문 여부(이때 비트 마스킹 사용.)이며
구체적인 경로, 도시의 방문 순서는 중요하지 않다.

2. 중복 확인

특정 start, last, V에서 이들을 활용한 find_path(start, last, V)가 실제 중복 호출되는지 확인해야! 이것이 확인되어야 동적 계획법이 실효성을 갖는다.
tmp_dist는? 여기서는 필요 X.

start, last, V에 find_path => 특정 start, last, V에 대해 아직 방문하지 않은 모든 도시 각각을 방문하는 재귀함수를 호출하고 이 중 최솟값을 취한다.

실제로 식을 점화하면 수많은 재귀호출이 발생. ex: 도시 개수가 10개라고 하면,
find_path(1, 2, {1, 3, 2}), find_path(1, 3, {1,2,3})이 호출될 때 각 함수는 모두 find_path(1, 4, {1, 2, 3, 4})를 호출.

현재 세 개의 변수를 사용하는데 start, last는 도시의 수 N을 따라가고 방문 여부 집합은 0과 1을 담기 때문에 2**N개의 상태를 가진다. 따라서 캐시 크기는 N*N*2**N = (n**2)*(2**N)이 된다.

3. 시작 도시조차 중요 X.

한 번 방문한 도시는 재방문 X. => 시작점을 단일 도시로 고정해도 괜춘! 따라서 우리가 관리해야 할 변수는 총 2개.

"""

def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N) - 1
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')
    
    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]
            
        tmp = INF        
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp,
		 	  find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp
                
    return find_path(0, 1 << 0)

from sys import stdin

input = stdin.readline

N = int(input())
dis = []
for _ in range(N):
    a = list(map(int, input().split()))
    dis.append(a)

print(tsp(dis))