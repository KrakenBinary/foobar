#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
lets get-r-done! Space cowboy math here!
'''


def solution(xs):
    '''Time to hotwire some panels my guy!'''
    result = 1
    zeros = [item for item in xs if item == 0]
    negatives = [item for item in xs if item < 0]
    positives = [item for item in xs if item > 0]
    if len(negatives) == 1 > len(positives) < len(zeros):
        return str(0)
    if len(positives) > 0 or (len(positives) < 1 < len(negatives)):
        if len(negatives) % 2 != 0:
            negatives.remove(max(negatives))
    result_array = negatives + positives
    if len(result_array) == 0:
        return str(0)
    for number in result_array:
        result *= number
    return str(result)


print(solution([2, 0, 2, 2, 0]))    # 8
print(solution([-4]))               # -4    case 3
print(solution([-4, 0]))            # 0     case 5
print(solution([-4, 0, 0, 0, 0]))   # 0     case 5
print(solution([-4, -4]))           # 16
print(solution([-4, -4, -4]))       # 16
print(solution([0]))                # 0
print(solution([1]))                # 1
print(solution([2]))                # 2
print(solution([-2, -3, 4, -5]))    # 60
print(solution([-2, 0, 0, -5, 0, 0, 10, 0, 0]))  # 100
print(solution([6, -3, -10, 0, 2]))  # 360
print(solution([-1, -3, -10, 0, 60]))  # 60
print(solution([-2, -40, 0, -2, -3]))  # 80
