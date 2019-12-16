# coding=utf-8

from node import Node
from algorithms import BreadthFirst,  UniformCostSearch, DepthFirst, DepthFirstLimited, DepthFirstLimitedIterative, \
    GreedySearch, ASearch

lim_depth = 12

# Per labirinto
max_depth = 13


#Stato iniziale contiene la città di partenza
state = [[1, 2, 3, 5, 0, 4, 8, 7, 6], [1, 1]]

#Obiettivo la città di arrivo
goal_state = [[1, 2, 3, 4, 5, 6, 7, 8, 0], [2, 2]]

#Genero nodo root
root = Node(0, state, None, 0)

#Eseguo algoritmo di ricerca
scelta=1
while scelta is not 0:
    #print("0)Esci\n1)BFS\n2)Uniform\n3)DFS\n4)DFS Limited \n5)DFS Limited Iterative\n6)Greedy\n7)A*\n")
    scelta=int(input('Scegli algoritmo: '))
    #print(scelta)
    if scelta == 1:
        BreadthFirst(root, goal_state)
    if scelta == 2:
        UniformCostSearch(root, goal_state)
    if scelta == 3:
        DepthFirst(root, goal_state)
    if scelta == 4:
        print("Soluzione DepthFirstLimited:")
        found = DepthFirstLimited(root, goal_state, lim_depth)
        if found == False:
            print("Soluzione non trovata")
    if scelta == 5:
        DepthFirstLimitedIterative(root, goal_state, max_depth)
    if scelta == 6:
        GreedySearch(root, goal_state)
    if scelta == 7:
        ASearch(root, goal_state)

