#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
matrix with a time of 1
  0  1  2  3  4
0[0, 2, 2, 2,-1]
1[9, 0, 2, 2,-1]
2[9, 3, 0, 2,-1]
3[9, 3, 2, 0,-1]
4[9, 3, 2, 2, 0]

If I want to move from 0 to another place I need to build an intermediate
matrix that checks for shortest path.

We keep the row/col of our position. calculating the other moves.
  0  1  2  3  4
0[0, 2, 2, 2,-1]
1[9, 0,  ,  ,  ]
2[9,  , 0,  ,  ]
3[9,  ,  , 0,  ]
4[9,  ,  ,  , 0]

[1,2] = [1,0]+[0,2]
  2 ?<=>? 9  +  2

we discover for [1,2] that the existing value is less that the "alternatives"
so we use the original value. Lets fill all of them in.

This is the Floyd-Warshall algorythm:
    A^k[i,j]=min{A^k-1[i,j],A^k-1[i,k]+A^k-1[k,j]}
    https://www.youtube.com/watch?v=oNI0rf2P9gE
    https://www.youtube.com/watch?v=4OQeCuLYj-4
'''


import itertools


def floyd_warshall(matrix):
    rows = len(matrix)
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix


def convert_to_path(permutations):
    '''as in the example above, we can build a path to check min on'''
    permutations = list(permutations)
    permutations = [0] + permutations + [-1]
    path = list()
    for i in range(1, len(permutations)):
        path.append((permutations[i - 1], permutations[i]))
    return path


def solution(time, time_limit):
    '''Floyd-Warshall algorythm (from notes above) goes here'''
    rows = len(time)
    bunnies = rows - 2  # take out the start and door

    time = floyd_warshall(time)

    # first make sure you dont have a red herring (test7 (hidden))
    for self in range(rows):
        if time[self][self] != 0:  # should take 0 time to move to self
            return list(i for i in range(bunnies))

    for i in reversed(range(bunnies + 1)):
        # r-length tuples, all possible orderings, no repeated elements
        for permutations in itertools.permutations(range(1, bunnies + 1), i):
            total_time = 0
            # print(perm)
            # for each non-repeating tuple, we send it to build a path
            path = convert_to_path(permutations)
            # now that we have a list of viable pats, we need to crawl time
            for start, end in path:
                total_time += time[start][end]
            if total_time <= time_limit:
                return sorted(list(i - 1 for i in permutations))
    return None


def neg_cycle_floyd_warshall(matrix):
    '''
    short_out stores shortest distances for the permutations
        Add all vertices one by one to the set of intermediate vertices.
        Before start of a iteration, we have shortest distances between
        all pairs of vertices such that the shortest distances consider
        only the vertices in set {0, 1, 2, .. k-1} as intermediate vertices.
        After the end of a iteration, vertex no. k is added to the set of
        intermediate vertices and the set becomes {0, 1, 2, .. k}
    '''
    verticies = len(matrix)
    short_out = [[0 for i in range(verticies+1)]for j in range(verticies+1)]

    for i in range(verticies):
        for j in range(verticies):
            short_out[i][j] = matrix[i][j]

    short_out = floyd_warshall(short_out)

    # now check for a negative weight cycle
    for i in range(verticies):
        if short_out[i][i] < 0:
            return True

    return False
