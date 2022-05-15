#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
test
'''


def floyd_warshall(matrix):
    '''main solution space'''
    rows = len(matrix)
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix


def solution(entrances, exits, path):
    '''main solution space'''
    # lets initialize the residual grid with our existing one
    residual = path[:]
    bunnies_escape = 0
    current_bunnies = -1
    while current_bunnies != bunnies_escape:
        print('-=TAG-1=-')
        print('{} | {}'.format(current_bunnies, bunnies_escape))
        current_bunnies = bunnies_escape
        # Check all paths starting at each available entrance
        for node in entrances:
            print('-=TAG-2=-')
            visited = []
            path = []
            while True:
                print('-=TAG-3=-')
                new_location = False
                visited.append(node)
                maximum = 0
                index = 0
                for i in range(len(residual[node])):
                    if residual[node][i] > maximum and i not in visited:
                        maximum = residual[node][i]
                        index = i
                        new_location = True
                if new_location:
                    path.append(node)
                    node = index
                elif not path:
                    print('-=BREAK-1=-')
                    break
                else:
                    node = path.pop()
                if node in exits:
                    path.append(node)
                    minimum = 2000000
                    for k in range(len(path) - 1):
                        if residual[path[k]][path[k + 1]] < minimum:
                            minimum = residual[path[k]][path[k + 1]]
                    bunnies_escape += minimum
                    for k in range(len(path) - 2):
                        residual[path[k]][path[k + 1]] -= minimum
                        residual[path[k + 1]][path[k]] += minimum
                    residual[path[len(path) - 2]][path[len(path) - 1]] -= minimum
                    print('-=BREAK-2=-')
                    break
    # Return number of bunnies
    print('-=RETURNING=-')
    return bunnies_escape


if __name__ == "__main__":
    # execute only if run as a script
    solution(
                [0],
                [3],
                [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]])
