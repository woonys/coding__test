from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) -1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1]> a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        left = last
        #left = last가 되면 for문 종료하고 아래 for문 동작!
        for j in range(left, right):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
            # 한 번 돌고나면 for문 종료하고 윗 for문이 동작!
        right = last

