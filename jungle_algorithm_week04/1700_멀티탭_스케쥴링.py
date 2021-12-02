# from sys import stdin
# input = stdin.readline

# N, K = map(int, input().split())
# app = list(map(int, input().split()))
# # 중복 리스트

# apps = list(set(app))
# count_apps = [0] * (K+1)
# for i in apps:
#     count_apps[i] +=app.count(i)

# consent = [0] * (N)
# cnt = 0
# for idx in range(len(apps)):
#     i = apps[idx]
#     new_insert = [i, count_apps[i]]
            
#     # 새로 끼우는 상황
#     if 0 in consent:
#         for k in range(N):
#             old_insert = consent[k]
#             if old_insert == 0:
#                 count_apps[i]-=1 # 차감 먼저 하고 삽입
#                 new_insert[1] -= 1
#                 consent[k] = new_insert
#                 break
                    
    
#     else: # 이미 끼워져 있는 상황
        
#         # 이미 끼워져 있는 애랑 동일하면
#         for old_i in range(N):
#             old_insert = consent[old_i]
            
#             if new_insert in consent:
#                 if old_insert[0] == new_insert[0]:
#                     old_insert[1] -=1
#                     count_apps[i] -= 1
#                     break
            
#             # 기존에 끼워져 있는 애랑 다른 애를 끼워야 할 때
#             # 
#             else:
#                 for l in range(idx+1, len(apps)):
#                     con_cnt = [0] * N
#                     for p in consent:
#                         if apps[l] == p[0]:
#                             con_cnt[apps[l]] = apps.index(apps[l])

#                     count_apps[last]-=1 # 차감 먼저 하고 삽입
#                     new_insert[1] -= 1
#                     consent[-1] = new_insert
#                     cnt += 1
#                     break    
                
                
# print(cnt)


###다시###

from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

multap = [0] * N
li = list(map(int, input().split()))
res = swap = num = max_I = 0

for i in li:
    # 이미 i가 멀티탭에 끼워져 있다면
    if i in multap:
        pass
    # 멀티탭에 빈 칸이 있다면 0인 곳에 배정
    elif 0 in multap:
        multap[multap.index(0)] = i
    # i가 멀티탭에 안 끼워져 있고 빈 칸도 없는 상황
    else:
        for j in multap: # 멀티탭을 쭉 스캔
            if j not in li[num:]: # num부터 쭉 스캔 => 처음에는 num == 0 => for 문 한바꾸 돌 떄마다 스캔 위치를 위로 올려
                swap = j
                break
            elif li[num:].index(j) > max_I:
                max_I = li[num:].index(j)
                swap = j
        multap[multap.index(swap)] = i
        max_I = swap = 0
        res += 1
    num += 1
print(res)
        
