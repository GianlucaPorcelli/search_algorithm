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
        self.heuristic = math.sqrt(pow(self.state[0] - goal[0], 2) + pow(self.state[1] - goal[1], 2))
        return self.heuristic