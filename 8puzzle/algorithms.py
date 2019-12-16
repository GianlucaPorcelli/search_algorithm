# coding=utf-8

import queue
from help import verifica_goal, gen_figli, print_path, print_puzzle#, minimum
from operator import attrgetter



def BreadthFirst(root, goal_state):
    print("Soluzione BreadthFirst:")
    coda = queue.Queue()

    # Aggiungo il nodo root alla coda
    coda.put(root)

    # Lista contenente i nodi visitati
    visited = []

    while not coda.empty():
    #for i in range (0,4):
        # Prendo il primo elemento nella coda
        nodo = coda.get()
        #print("Nodo in esame: ", nodo.state)
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo, goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo, goal_state[0])
            print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state[0], nodo.depth])
        #print(nodo.state)
        # Esploro il nodo che sto considerando
        gen_figli(nodo, coda, visited, 1, goal_state)

    print ("Soluzione non trovata")

def UniformCostSearch(root, goal_state):
    print("Soluzione UniformCostSearch:")
    coda = []

    # Aggiungo il nodo root alla coda
    coda.append([root.pathCost, root])
    # Lista contenente i nodi visitati
    visited = []

    #for i in range (0,2):
    while coda:
        # Prendo l'elemento nella coda con priorità più alta
        nodo = coda.pop()
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo[1], goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo[1], goal_state[0])
            print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo[1].state[0], nodo[1].pathCost])
        # Esplodo il nodo che sto considerando
        gen_figli(nodo[1], coda, visited, 2, goal_state)

        # Ordino da priorità bassa a priorità alta
        coda = sorted(coda, key=Take, reverse=True)
        # print(coda)
        #coda.sort(key=lambda x: x.count, reverse=True)
        #coda.sort(reverse=True)

    print ("Soluzione non trovata")

def Take(elem):
    return elem[0]

def DepthFirst(root, goal_state):
    print("Soluzione DepthFirst:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = queue.LifoQueue()

    # Aggiungo il nodo root alla coda
    coda.put(root)

    # Lista contenente i nodi visitati
    visited = []

    while not coda.empty():
        # Prendo il primo elemento nella coda
        nodo = coda.get()
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo, goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo, goal_state[0])
            print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state[0], nodo.depth])
        # Esplodo il nodo che sto considerando
        gen_figli(nodo, coda, visited, 1, goal_state)
    print ("Soluzione non trovata")

def DepthFirstLimited(root, goal_state, lim_depth):
    #print("Soluzione DepthFirstLimited:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = queue.LifoQueue()

    # Aggiungo il nodo root alla coda
    coda.put(root)

    # Lista contenente i nodi visitati
    visited = []

    while not coda.empty():
        # Prendo il primo elemento nella coda
        nodo = coda.get()

        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo, goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo, goal_state[0])
            print_puzzle(root, goal_state[0])
            return True
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state[0], nodo.depth])
        #Verifico a che profondità mi trovo
        if nodo.depth < lim_depth:
            # Esplodo il nodo che sto considerando
            gen_figli(nodo, coda, visited, 1, goal_state)
            #Elimino da visited i nodi già controllati

    return False

def DepthFirstLimitedIterative(root, goal_state, max_depth):
    print("Soluzione DepthFirstLimitedIterative:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = queue.LifoQueue()

    for i in range(0, max_depth):
        found = False

        #Richiamo DepthFirstLimited
        found = DepthFirstLimited(root, goal_state, i)

        if found == True:
            break
    if found == False:
        print("Soluzione non trovata")
    else:
        print("Depth:", i)

#------------------------- ALGORITMI RICERCA INFORMATA -----------------------------------------------------------#

#Eseguo per primi gli elementi meno distanti dal goal
def GreedySearch(root, goal_state):
    print("Soluzione Greedy:")
    coda = []
    #print(goal_state[0])
    # Aggiungo il nodo root alla coda
    coda.append([root.set_heuristic(goal_state[0]), root])
    print("Heur", root.heuristic)
    # Lista contenente i nodi visitati
    visited = []

    #for i in range(0,1):
    while coda:
        # Prendo l'elemento nella coda con priorità più alta
        nodo = coda.pop()
        print(nodo[1].heuristic)
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo[1], goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo[1], goal_state[0])
            print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo[1].state[0], nodo[1].depth])
        # Esplodo il nodo che slto considerando
        gen_figli(nodo[1], coda, visited, 3, goal_state)
        # Ordino da priorità bassa a priorità alta
        coda = sorted(coda, key=Take, reverse=True)
    print ("Soluzione non trovata")

#Eseguo per primi gli elementi meno distanti dal goal
def ASearch(root, goal_state):
    print("Soluzione A*:")
    coda = []

    # Aggiungo il nodo root alla coda
    coda.append([root.set_heuristic(goal_state[0]), root])
    # Lista contenente i nodi visitati
    visited = []

    while coda:
        # Prendo l'elemento nella coda con priorità più alta
        nodo = coda.pop()
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo[1], goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print("Soluzione Trovata")
            print_path(nodo[1], goal_state[0])
            print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo[1].state[0], nodo[1].pathCost])
        # Esplodo il nodo che slto considerando
        gen_figli(nodo[1], coda, visited, 4, goal_state)
        # Ordino da priorità bassa a priorità alta
        coda = sorted(coda, key=Take, reverse=True)

#Todo: Vedere problema di python 3 nell ordinamento della lista
#Todo: Cancellazione nodi nel DepthFirst