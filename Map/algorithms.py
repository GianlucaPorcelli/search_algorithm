# coding=utf-8

import Queue
from help import verifica_goal, gen_figli, print_path, print_puzzle#, minimum



def BreadthFirst(root, goal_state, list):
    print("Soluzione BreadthFirst:")
    coda = Queue.Queue()

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
            #Todo: Inserire funzione per stampare percorso
            print_path(nodo)
            # print_puzzle(root, goal_state[0])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state,nodo.depth])
        #print(nodo.state)
        # Esploro il nodo che sto considerando
        gen_figli(nodo, coda, visited, 1, goal_state, list)

    print ("Soluzione non trovata")

def UniformCostSearch(root, goal_state, list):
    print("Soluzione UniformCostSearch:")
    coda = []

    # Aggiungo il nodo root alla coda
    coda.append([root.pathCost, root])
    # Lista contenente i nodi visitati
    visited = []

    while coda:
        # Prendo l'elemento nella coda con priorità più alta
        nodo = coda.pop()
        # Verifica se è il nostro obiettivo
        print (nodo[1].state)
        found = verifica_goal(nodo[1], goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print_path(nodo[1])
            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append(nodo[1])
        # Esplodo il nodo che sto considerando
        gen_figli(nodo[1], coda, visited, 2, goal_state, list)

        # Ordino da priorità bassa a priorità alta
        coda.sort(reverse=True)
        for i in range(0,len(coda)):
            print(coda[i])
    print ("Soluzione non trovata")

def DepthFirst(root, goal_state, list):
    print("Soluzione DepthFirst:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = Queue.LifoQueue()

    # Aggiungo il nodo root alla coda
    coda.put(root)

    # Lista contenente i nodi visitati
    visited = []

    while not coda.empty():
        # Prendo il primo elemento nella coda
        nodo = coda.get()
        print(nodo.state)
        # Verifica se è il nostro obiettivo
        found = verifica_goal(nodo, goal_state)
        # Se ho trovato l'obiettivo è inutile andare avanti
        if found == True:
            print_path(nodo)

            return
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state,nodo.depth])
        # Esplodo il nodo che sto considerando
        gen_figli(nodo, coda, visited, 1, goal_state, list)
    print ("Soluzione non trovata")

def DepthFirstLimited(root, goal_state,list, lim_depth):
    #print("Soluzione DepthFirstLimited:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = Queue.LifoQueue()

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
            print_path(nodo)
            return True
        # Aggiungo alla lista il nodo che sto esplorando
        visited.append([nodo.state,nodo.depth])
        #Verifico a che profondità mi trovo
        if nodo.depth < lim_depth:
            # Esplodo il nodo che sto considerando
            gen_figli(nodo, coda, visited, 1, goal_state, list)
            #Elimino da visited i nodi già controllati

    return False

def DepthFirstLimitedIterative(root, goal_state, list, max_depth):
    print("Soluzione DepthFirstLimitedIterative:")

    # Nel DepthFirst viene utilizzata la LIFO per la ricerca nella frontiera
    coda = Queue.LifoQueue()

    for i in range(0, max_depth):
        found = False

        #Richiamo DepthFirstLimited
        found = DepthFirstLimited(root, goal_state, list, i)

        if found == True:
            break
    if found == False:
        print("Soluzione non trovata")
    else:
        print("Depth:", i)

# #------------------------- ALGORITMI RICERCA INFORMATA -----------------------------------------------------------#
#
# #Eseguo per primi gli elementi meno distanti dal goal
# def GreedySearch(root, goal_state, x, y, costi):
#     print("Soluzione Greedy:")
#     coda = []
#
#     # Aggiungo il nodo root alla coda
#     coda.append([root.set_heuristic(goal_state[0]), root])
#     print("Heur", root.heuristic)
#     # Lista contenente i nodi visitati
#     visited = []
#
#     #for i in range(0,100):
#     while coda:
#         # Prendo l'elemento nella coda con priorità più alta
#         nodo = coda.pop()
#         print(nodo[1].heuristic)
#         # Verifica se è il nostro obiettivo
#         found = verifica_goal(nodo[1], goal_state)
#         # Se ho trovato l'obiettivo è inutile andare avanti
#         if found == True:
#             # TODO: Vedere come stampare il percorso
#             print_path(nodo[1], goal_state[0])
#             print_puzzle(root, goal_state[0])
#             return
#         # Aggiungo alla lista il nodo che sto esplorando
#         visited.append(nodo[1])
#         # Esplodo il nodo che slto considerando
#         gen_figli(nodo[1], coda, visited, x, y, costi, 3, goal_state)
#         # Ordino da priorità bassa a priorità alta
#         coda.sort(reverse=True)
#         #minimum(coda,0)
#
# #Eseguo per primi gli elementi meno distanti dal goal
# def ASearch(root, goal_state, x, y, costi):
#     print("Soluzione A*:")
#     coda = []
#
#     # Aggiungo il nodo root alla coda
#     coda.append([root.set_heuristic(goal_state[0]), root])
#     # Lista contenente i nodi visitati
#     visited = []
#
#     while coda:
#         # Prendo l'elemento nella coda con priorità più alta
#         nodo = coda.pop()
#         # Verifica se è il nostro obiettivo
#         found = verifica_goal(nodo[1], goal_state)
#         # Se ho trovato l'obiettivo è inutile andare avanti
#         if found == True:
#             # TODO: Vedere come stampare il percorso
#             print_path(nodo[1], goal_state[0])
#             print_puzzle(root, goal_state[0])
#             return
#         # Aggiungo alla lista il nodo che sto esplorando
#         visited.append(nodo[1])
#         # Esplodo il nodo che slto considerando
#         gen_figli(nodo[1], coda, visited, x, y,costi, 4, goal_state)
#         # Ordino da priorità bassa a priorità alta
#         coda.sort(reverse=True)
#         #minimum(coda,0)

#Todo: Vedere problema di python 3 nell ordinamento della lista
#Todo: Cancellazione nodi nel DepthFirst