from sys import stdin

N = int(stdin.readline())

pos = [0] * N #각 열에 배치한 퀸의 위치
flag_a = [False] * N #각 행에 퀸을 배치했는지 체크
flag_b = [False] * (2*N-1) #(2* N - 1)  => 오른쪽 대각선 방향으로 퀸을 배치했는지 체크 // 최대
flag_c = [False] * (2*N-1) # 왼쪽 대각선 방향으로 퀸을 배치했는지 체크
count = 0
def put() -> None:
    for i in range(N):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    for j in range(N):
        if (    not flag_a[j]
            and not flag_b[i+j]
            and not flag_c[i-j+(N-1)]):
            pos[i] = j
            if i == (N-1):
                put()
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+(N-1)] = False


set(0)