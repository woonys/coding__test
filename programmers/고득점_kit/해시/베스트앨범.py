'''
How to solve: 내 손으로 풀이
시간복잡도: O(N)
공간복잡도: O(N)
풀이 시간: 시간 초과 -> why? 일일이 로직짜는데 시간이 오래 걸림..
다시 생각해보기 -> 일단 넣고 그다음 min 함수로 잘라내는 게 낫지  않을까
'''

# from collections import defaultdict
# def solution(genres, plays):
#     length = len(genres)
#     dic = defaultdict(list)
#     set_genres = set(genres)
#     for i in set_genres:
#         dic[i] = [-1, -1, 0] # 가장 큰 값 인덱스, 가장 작은 값 인덱스, 재생 횟수

#     # dic에 다 넣음

#     for i in range(length): 
#         this_gen = genres[i]
#         this_play = plays[i]
#         first_song_idx = dic[this_gen][0]
#         second_song_idx = dic[this_gen][1]

#         dic[this_gen][2] += this_play
#         # 처음
#         if first_song_idx == -1 and second_song_idx == -1:
#             dic[this_gen][0] = i
#         elif first_song_idx != -1 and second_song_idx == -1:
#             if this_play > plays[first_song_idx]:
#                 dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
#             else: # 작거나 같다면 뒤로 밀려나야 된다.
#                 dic[this_gen][1] = i
#         elif first_song_idx != -1 and second_song_idx != -1:
#             if plays[first_song_idx] > plays[second_song_idx]:
#                 if this_play > plays[first_song_idx]:
#                     dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
#                 elif this_play == plays[first_song_idx]:
#                     dic[this_gen][1] = i
#                 elif this_play < plays[first_song_idx]:
#                     if this_play > plays[second_song_idx]:
#                         dic[this_gen][1] = i
#                     else:
#                         continue
#             elif plays[first_song_idx] == plays[second_song_idx]:
#                 if this_play > plays[first_song_idx]:
#                     dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
#                 elif this_play == plays[first_song_idx]:
#                     continue
#                 elif this_play < plays[first_song_idx]:
#                     if this_play > plays[second_song_idx]:
#                         dic[this_gen][1] = i
#                     else:
#                         continue
#     dic_to_li = list(zip(dic.keys(),dic.values()))
#     dic_to_li.sort(key= lambda x: -x[1][2])

#     answer = []

#     for i in dic_to_li:
#         first = i[1][0]
#         second = i[1][1]
#         if second == -1:
#             answer.append(first)
#         else:
#             answer.append(first)
#             answer.append(second)

#     return answer


def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))