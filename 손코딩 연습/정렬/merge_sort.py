'''
Merge sort

두 개의 메소드가 필요!
1) merge: 두 리스트를 비교 후 정렬하는 메소드
2) merge_sort: 리스트를 계속해서 분할한 다음 merge()를 수행시켜 최종적으로 정렬하는 메소드
'''

li = [1, 7, 6, 8, 2, 9, 3]

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftlist = list[:mid]
    rightlist = list[mid:]
    leftlist = merge_sort(leftlist)
    rightlist = merge_sort(rightlist)
    
    return merge(leftlist, rightlist)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:] # left 맨 왼쪽 값을 result에 넣었으니 해당 값 빼고 left 갱신
            else:
                result.append(right[0])
                right = right[1:] # right 맨 왼쪽 값을 result에 넣었으니 해당 값 빼고 right 갱신
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

print(merge_sort(li))

## 연습 -> 1번 더!

def merge_sort(list):
    # 예외 케이스
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    
    # 나누기
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            # left, right는 이미 정렬된 상태
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
        return result