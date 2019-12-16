# coding=utf-8

from node import Node
from algorithms import BreadthFirst, UniformCostSearch, DepthFirst, DepthFirstLimited, DepthFirstLimitedIterative #, \
    GreedySearch#, ASearch

lim_depth = 5

# Per labirinto
max_depth = 2


#Stato iniziale contiene la città di partenza
state = 'Timisoara'

#Obiettivo la città di arrivo
goal_state = 'Bucharest'

list = [['Arad', 'Zerind', 75], ['Timisoara', 'Arad', 118], ['Arad', 'Sibiu', 140],
        ['Zerind', 'Oradea', 71], ['Oradea', 'Sibiu', 151], ['Sibiu', 'Rimnicu Vilcea', 80],
        ['Timisoara', 'Lugoj', 111], ['Lugoj', 'Mehadia', 70], ['Mehadia', 'Dobreta', 75],
        ['Dobreta', 'Craiova', 120], ['Craiova', 'Rimnicu Vilcea', 146], ['Craiova', 'Pitesti', 138],
        ['Fagaras', 'Sibiu', 99], ['Rimnicu Vilcea', 'Pitesti', 97], ['Fagaras', 'Bucharest', 211],
        ['Pitesti', 'Bucharest', 101]]


#Genero nodo root
root = Node(0,state,None,0)

#Eseguo algoritmo di ricerca
scelta=1
while scelta is not 0:
    #print("0)Esci\n1)BFS\n2)Uniform\n3)DFS\n4)DFS Limited \n5)DFS Limited Iterative\n6)Greedy\n7)A*\n")
    scelta=int(input('Scegli algoritmo: '))
    #print(scelta)
    if scelta == 1:
        BreadthFirst(root, goal_state, list)
    if scelta == 2:
        UniformCostSearch(root, goal_state, list)
    if scelta == 3:
        DepthFirst(root, goal_state, list)
    if scelta == 4:
        print("Soluzione DepthFirstLimited:")
        found = DepthFirstLimited(root, goal_state, list, lim_depth)
        if found == False:
            print("Soluzione non trovata")
    if scelta == 5:
        DepthFirstLimitedIterative(root, goal_state, list, max_depth)
    # if scelta == 6:
    #     GreedySearch(root, goal_state, list)
    # if scelta == 7:
    #     ASearch(root, goal_state, dim_x, dim_y, costi)

