#!/usr/bin/python3
# -*- coding:utf-8 -*-

# import math
import sys


class EscapePods:
    INF = sys.maxsize

    @staticmethod
    def transform(sources, sinks, network):
        # transform to a equivalent single-source, single-sink flow network
        length = len(network)
        newLength = length + 2
        newNetwork = [[0] * (newLength) for _ in range(newLength)]
        i = 0
        while (i < length):
            j = 0
            while (j < length):
                newNetwork[i + 1][j + 1] = network[i][j]
                j += 1
            i += 1
        for entrance in sources:
            newNetwork[0][entrance + 1] = EscapePods.INF
        for exit in sinks:
            newNetwork[exit + 1][newLength - 1] = EscapePods.INF
        return newNetwork

    @staticmethod
    def bfs(residual_network):
        # find path from s to t | every (u, v) in p satisfies c_f(u, v) > 0
        parents = [0] * (len(residual_network))
        Arrays.fill(parents, -1)
        queue = java.util.ArrayDeque()
        queue.append(0)
        u = 0
        while (not queue.isEmpty() and parents[len(parents) - 1] == -1):
            u = queue.pop(0)
            v = 0
            while (v < len(parents)):
                if (residual_network[u][v] > 0 and parents[v] == -1):
                    queue.append(v)
                    parents[v] = u
                v += 1
        path = []
        u = parents[len(parents) - 1]
        while (u != 0):
            if (u == -1):
                return None
            path.add(u)
            u = parents[u]
        Collections.reverse(path)
        return path

    @staticmethod
    def solveWithFordFulkerson(residual_network):
        # https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
        max_flow = 0
        path = EscapePods.bfs(residual_network)
        while path is not None:
            # calculate residual capacity c_f(p)
            residual_capacity = EscapePods.INF
            u = 0
            for v in path:
                residual_capacity = min(residual_capacity, residual_network[u][v])
                u = v
            # increment max flow
            max_flow += residual_capacity
            u = 0
            # update residual network
            for v in path:
                residual_network[u][v] -= residual_capacity
                residual_network[v][u] += residual_capacity
                u = v
        return max_flow

    @staticmethod
    def solution(entrances, exits, path):
        return EscapePods.solveWithFordFulkerson(EscapePods.transform(entrances, exits, path))
