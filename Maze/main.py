# coding=utf-8

from node import Node
from algorithms import BreadthFirst, UniformCostSearch , DepthFirst, DepthFirstLimited, DepthFirstLimitedIterative, \
    GreedySearch, ASearch

#Condizioni iniziali:
#Potrebbero essere impostate dall'utente
dim_x = 6
dim_y = 5
muri = [[0, 4], [1, 1], [2, 0], [2, 1], [2, 3], [3, 3], [4, 1]]
lim_depth = 11
# Per labirinto
max_depth = (dim_y * dim_y)

#Stato iniziale
state = [0, 0]
#Obiettivo
goal_state = [5, 1]

#Genero nodo root
root = Node(0,state,None,0)

#Eseguo algoritmo di ricerca
scelta=1
while scelta is not 0:
    print("0)Esci\n1)BFS\n2)Uniform\n3)DFS\n4)DFS Limited \n5)DFS Limited Iterative\n6)Greedy\n7)A*\n")
    scelta=int(input('Scegli algoritmo: '))
    print(scelta)
    if scelta == 1:
        BreadthFirst(root, goal_state, dim_x, dim_y, muri)
    if scelta == 2:
        UniformCostSearch(root, goal_state, dim_x, dim_y, muri)
    if scelta == 3:
        DepthFirst(root, goal_state, dim_x, dim_y, muri)
    if scelta == 4:
        print("Soluzione DepthFirstLimited:")
        found = DepthFirstLimited(root, goal_state, dim_x, dim_y, muri, lim_depth)
        if found == False:
            print("Soluzione non trovata")
    if scelta == 5:
        DepthFirstLimitedIterative(root, goal_state, dim_x, dim_y, muri, max_depth)
    if scelta == 6:
        GreedySearch(root, goal_state, dim_x, dim_y, muri)
    if scelta == 7:
        ASearch(root, goal_state, dim_x, dim_y, muri)

