'''
How to solve: 내 손으로 풀이
시간복잡도: O(N)
공간복잡도: O(N)
풀이 시간: 시간 초과 -> why? 일일이 로직짜는데 시간이 오래 걸림..
다시 생각해보기 -> 일단 넣고 그다음 min 함수로 잘라내는 게 낫지  않을까

or 로직 분리 -> dict에 넣을 때 처음부터 순서 다 배열해서 넣는게 아니라
일단 각 노래별로 [인덱스, 재생횟수]를 넣고난 다음
그 안에서 재생횟수 별로 정렬하는 것이 더 간결했을 듯. 
'''
# 1. my solution

from collections import defaultdict
def solution(genres, plays):
    length = len(genres)
    dic = defaultdict(list)
    set_genres = set(genres)
    for i in set_genres:
        dic[i] = [-1, -1, 0] # 가장 큰 값 인덱스, 가장 작은 값 인덱스, 재생 횟수

    # dic에 다 넣음

    for i in range(length): 
        this_gen = genres[i]
        this_play = plays[i]
        first_song_idx = dic[this_gen][0]
        second_song_idx = dic[this_gen][1]

        dic[this_gen][2] += this_play
        # 처음
        if first_song_idx == -1 and second_song_idx == -1:
            dic[this_gen][0] = i
        elif first_song_idx != -1 and second_song_idx == -1:
            if this_play > plays[first_song_idx]:
                dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
            else: # 작거나 같다면 뒤로 밀려나야 된다.
                dic[this_gen][1] = i
        elif first_song_idx != -1 and second_song_idx != -1:
            if plays[first_song_idx] > plays[second_song_idx]:
                if this_play > plays[first_song_idx]:
                    dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
                elif this_play == plays[first_song_idx]:
                    dic[this_gen][1] = i
                elif this_play < plays[first_song_idx]:
                    if this_play > plays[second_song_idx]:
                        dic[this_gen][1] = i
                    else:
                        continue
            elif plays[first_song_idx] == plays[second_song_idx]:
                if this_play > plays[first_song_idx]:
                    dic[this_gen][0], dic[this_gen][1] = i, first_song_idx
                elif this_play == plays[first_song_idx]:
                    continue
                elif this_play < plays[first_song_idx]:
                    if this_play > plays[second_song_idx]:
                        dic[this_gen][1] = i
                    else:
                        continue
    dic_to_li = list(zip(dic.keys(),dic.values()))
    dic_to_li.sort(key= lambda x: -x[1][2])

    answer = []

    for i in dic_to_li:
        first = i[1][0]
        second = i[1][1]
        if second == -1:
            answer.append(first)
        else:
            answer.append(first)
            answer.append(second)

    return answer


# 2. 다른 풀이: 매우 간결 but 실용적이지는 않은듯.
# 참고할 부분: zip, range(len(plays)) => 인덱스 뽑아내기
# 람다 사용 부분도 좋았음.
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))): # range(len(plays)): 인덱스 넣어주기!
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

# 3. 다른 풀이: 너무 함축적이지 않으면서 이해가능한 코드. 가장 좋은듯.

def solution(genres, plays):
    genres_dict = {}
    genres_list = []
    
    # 처음에 [인덱스, 재생횟수]별로 딕셔너리에 값 넣기
    for i in range(len(genres)):
        if genres[i] not in genres_dict:
            genres_dict[genres[i]] = []
        genres_dict[genres[i]].append([i, plays[i]])

    # 딕셔너리 내에서 각 장르별로 리스트 내 정렬 -> 다른 리스트에 해당 장르 전체 재생횟수 for문으로 돌려서 넣고
    for g in genres_dict:
        genres_dict[g].sort(key=lambda x: x[1], reverse=True)
        genres_list.append([g, sum([play for _, play in genres_dict[g]])])
    # 리스트 정렬 후에 
    genres_list.sort(key=lambda x: x[1], reverse=True)
    answer = []
    for g, _ in genres_list:
        answer.extend([x[0] for x in genres_dict[g][:2]])
    return answer