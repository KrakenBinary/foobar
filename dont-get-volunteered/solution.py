#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
Naturally the henchmen have to know how to play chess.
'''


def pos(location):
    '''
    To survive, I have to know if i am along a border,
    and what column and row am I currently on?
    '''
    row = location/8
    col = location % 8
    edge = bool(0 in {row, col} or 7 in {row, col})
    return [col, row, edge]


def solution(src, dest):
    '''
    lets handle the main movements here.
    and be quick about it! or else get fed to the LAMBCHOP
    '''
    bfs = [  # bfs plot of starting point, to corners.
        [0],
        [3, 2],
        [2, 1, 4],
        [3, 2, 3, 2],
        [2, 3, 2, 3, 4],
        [3, 4, 3, 4, 3, 4],
        [4, 3, 4, 3, 4, 5, 4],
        [5, 4, 5, 4, 5, 4, 5, 6]
    ]
    source = pos(src)
    destination = pos(dest)
    distance_x = int(abs(source[0] - destination[0]))
    distance_y = int(abs(source[1] - destination[1]))
    distance = [distance_x, distance_y]

    if (source[2] or destination[2]) and (distance == [1, 1]):
        return '4'
    if distance_x > distance_y:
        return bfs[distance_x][distance_y]
    return bfs[distance_y][distance_x]
