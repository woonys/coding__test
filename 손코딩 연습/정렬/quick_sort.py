'''
Quick sort

기준 데이터(pivot)을 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법.
일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나.
병합 정렬과 더불어 대부분 프로그래밍 언어의 정렬 라이브러리 근간
가장 기본적인 퀵 정렬: 첫 번쨰 데이터를 기준 데이터(pivot)으로 설정.

'''


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))