# coding=utf-8
import math

class Node(object):
    def __init__(self, pathCost, state, parent, depth):
        # state = stato attuale in quel nodo
        self.pathCost = pathCost
        self.state = state
        self.parent = parent
        self.depth = depth
        self.heuristic = 0



    def set_heuristic(self, goal):

        self.heuristic = 0
        gol = list(goal)
        for i in range(0, len(self.state[0])):
            if self.state[0][i] != gol[i]:
                self.heuristic += 1
        return self.heuristic