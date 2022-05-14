#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
after playing in the matrix, a little "reverse" engineering should be "quicker"
see what I did there... because division takes forever ... #dadjokes
'''


def solution(list_in):
    '''so many nested loops and division, it hurts my soul'''
    if len(list_in) < 3 or sum(list_in) < 1:
        return 0
    length = len(list_in)
    empty_array = [0] * length
    result = 0
    for i in range(length):
        for j in range(i+1, length):
            if list_in[j] != 0 and list_in[i] != 0:
                if list_in[j] % list_in[i] == 0:
                    empty_array[i] += 1
    for i in range(length):
        for j in range(i+1, length):
            if list_in[j] != 0 and list_in[i] != 0:
                if list_in[j] % list_in[i] == 0:
                    result += empty_array[j]
    return result


l0 = [2, 5, 1, 3, 0, 4, 3, 8]
a0 = 1

l1 = [1, 2, 3, 4, 5, 6]
a1 = 3

l2 = [1, 1, 1]
a2 = 1

l3 = [1, 1]
a3 = 0

l4 = [0, 0]
a4 = 0

l5 = [0, 0, 0]
a5 = 0

l6 = [1, 0, 0]
a6 = 0

l7 = [1, 1, 0]
a7 = 0

l8 = []
a8 = 0

print(solution(l0))
print(solution(l1))
print(solution(l2))
print(solution(l3))
print(solution(l4))
print(solution(l5))
print(solution(l6))
print(solution(l7))
print(solution(l8))
