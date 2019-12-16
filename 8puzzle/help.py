# coding=utf-8
import sys
from node import Node

#Funzione per verificare se ho raggiunto l'obiettivo
def verifica_goal(nodo, goal):
    # Verifico se ho raggiunto o meno l'obiettivo
    if nodo.state == goal:
        # Se l'obiettivo è stato raggiunto restituisco True
        return True
    else:
        return False

def print_path(nodo, goal):
    print("Costo totale: ", nodo.pathCost, "\n")
    path = []
    percorso = []
    while nodo.parent != None:
        path.append(nodo)
        nodo = nodo.parent
    for i in range(0, len(path)):
        percorso.append(path[i].state[0])
        print(percorso[i])
        print_puzzle(path[i], goal)
    return percorso

def print_puzzle(nodo, goal):
    posizione = 0
    state = nodo.state[0]
    for i in range(0, 3):
        for j in range(0, 3):
            if state[posizione] == 0:
                sys.stdout.write("| |")
                sys.stdout.write(" ")
            else:
                sys.stdout.write("|"+str(state[posizione]))
                sys.stdout.write("|")
                sys.stdout.write(" ")
            posizione += 1
        print(" ")
    #print("Distanza dal gol: ",distance(nodo.state,goal))
    print("\n")


#Funzione per generare i nodi figli
def gen_figli(padre, fringe, visitati, algo, goal):
    found = False
    # Prendo le coordinate della casella vuota
    zero = padre.state[1]

    # Verifico se posso andare giù
    if zero[0] + 1 < 3:
        #Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1 or algo == 3:
                if visitati[i][0] == set_state(padre.state, 3, [zero[0] + 1, zero[1]])[0] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break
            if algo == 2 or algo == 4:
                if visitati[i][0] == set_state(padre.state, 3, [zero[0] + 1, zero[1]])[0] and visitati[i][1] < padre.pathCost + 1:
                    found = True
                    break

        if found == False:
            #Genero il figlio e lo inserisco nella frontiera
            son = Node(padre.pathCost + 1, set_state(padre.state, 3, [zero[0] + 1, zero[1]]), padre, padre.depth + 1)
             #print(son.state[0], son.state[1])
            coda(fringe, son, algo, padre, goal)
            #print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare sopra
    if zero[0] - 1 >= 0:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1 or algo == 3:
                if visitati[i][0] == set_state(padre.state, -3, [zero[0] - 1, zero[1]])[0] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break
            if algo == 2 or algo == 4:
                if visitati[i][0] == set_state(padre.state, -3, [zero[0] - 1, zero[1]])[0] and visitati[i][1] < padre.pathCost + 2:
                    found = True
                    break
        if found == False:
            # Genero il figlio e lo inserisco nella frontiera
            son = Node(padre.pathCost + 2, set_state(padre.state, -3, [zero[0] - 1, zero[1]]), padre,
                       padre.depth + 1)
           # print(son.state[0], son.state[1])

            coda(fringe, son, algo, padre, goal)
            # print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare destra
    if zero[1] + 1 < 3:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1 or algo == 3:
                if visitati[i][0] == set_state(padre.state, 1, [zero[0], zero[1] + 1])[0] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break

            if algo == 2 or algo == 4:
                if visitati[i][0] == set_state(padre.state, 1, [zero[0], zero[1] + 1])[0] and visitati[i][1] < padre.pathCost + 3:
                    found = True
                    break

        if found == False:
            # Genero il figlio e lo inserisco nella frontiera
            son = Node(padre.pathCost + 3, set_state(padre.state, 1, [zero[0], zero[1] + 1]), padre, padre.depth + 1)
           # print(son.state[0], son.state[1])

            coda(fringe, son, algo, padre, goal)
            # print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare sinistra
    if zero[1] - 1 >= 0:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1 or algo == 3:
                if visitati[i][0] == set_state(padre.state, -1, [zero[0], zero[1] - 1])[0] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break
            if algo == 2 or algo == 4:
                if visitati[i][0] == set_state(padre.state, -1, [zero[0], zero[1] - 1])[0] and visitati[i][1] < padre.pathCost + 4:
                    found = True
                    break

        if found == False:
            # Genero il figlio e lo inserisco nella frontiera
            son = Node(padre.pathCost + 4, set_state(padre.state, -1, [zero[0], zero[1] - 1]), padre, padre.depth + 1)
           # print(son.state[0], son.state[1])

            coda(fringe, son, algo, padre, goal)
            # print("Nodo figlio sx: ", son.state)
        else:
            found = False

# Funzione per memorizzare il nodo in conda
def coda(fringe, figlio, type_algo, padre, goal):

    if type_algo == 1:
        # Inserisco nella queue
        fringe.put(figlio)
    if type_algo == 2:
        fringe.append([figlio.pathCost, figlio])
    if type_algo == 3:
        fringe.append([figlio.set_heuristic(goal[0]), figlio])
    if type_algo == 4:
        fringe.append([padre.pathCost + figlio.set_heuristic(goal[0]), figlio])

def set_state(state, mov, zero):
    # Devo cambiare lo zero con il terzo elemento che segueo lo zero nel vettore
    # Cambio la coordinata dello zero in un numero (rappresenta posizione all'interno del vettore)

    new_state = list(state)
    pos = change_coor(state[1])
    state2 = list(new_state[0])
    state2[pos] = state2[pos + mov]
    state2[pos + mov] = 0
    new_state[0] = state2
    new_state[1] = zero
    return new_state

# Funzione per stabilire la posizione dello zero nel vettore
def change_coor(state):
    if state == [0, 0]:
        return 0
    if state == [0, 1]:
        return 1
    if state == [0, 2]:
        return 2
    if state == [1, 0]:
        return 3
    if state == [1, 1]:
        return 4
    if state == [1, 2]:
        return 5
    if state == [2, 0]:
        return 6
    if state == [2, 1]:
        return 7
    if state == [2, 2]:
        return 8


























