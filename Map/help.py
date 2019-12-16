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

def print_path(nodo):
    print("Costo totale: ", nodo.pathCost,"\n")
    path = []
    percorso=[]
    while nodo.parent != None:
        path.append(nodo)
        nodo = nodo.parent
    for i in range(0,len(path)):
        percorso.append(path[i].state)
        print(percorso[i])
    return percorso

#Funzione per generare i nodi figli
def gen_figli(padre, fringe, visitati, algo, goal, list):
    found = False

    result = []
    #Trovo all'interno del grafo le città vicine alla città in esame
    for item in list:
        if padre.state in item:
            result.append(item)

    #Scorro la lista di tutte le città vicine
    for i in range(0,len(result)):
        # Andiamo a controllare se nella tripla la città da visitare è il primo o il secondo elemento
        # Controllo che la destinazione sia il secondo elemento della tripla
        if result[i][0] == padre.state:
            #Controllo se la destinazione è già presente in visitati
            for j in range(0,len(visitati)):
                if algo == 1:
                    if result[i][1] == visitati[j][0] and visitati[j][1] < padre.depth +1:
                        found = True
                        break

            if found == False:
                #Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + result[i][2], result[i][1], padre, padre.depth + 1)
                coda(fringe, son, algo, padre, goal)
                print("Nodo figlio sx: ", son.state)

        found = False

        # Controllo che la destinazione sia il primo elemento della tripla
        if result[i][1] == padre.state:
            # Controllo se la destinazione è già presente in visitati
            for j in range(0, len(visitati)):
                if algo == 1:
                    if result[i][0] == visitati[j][0] and visitati[j][1] < padre.depth +1:
                        found = True
                        break

            if found == False:
                # Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + result[i][2], result[i][0], padre, padre.depth + 1)
                coda(fringe, son, algo, padre, goal)
                print("Nodo figlio dx: ", son.state)
        found = False

# Funzione per memorizzare il nodo in conda
def coda(fringe, figlio, type_algo, padre, goal):

    if type_algo == 1:
        # Inserisco nella queue
        fringe.put(figlio)
    if type_algo == 2:
        fringe.append([figlio.pathCost, figlio])
    # if type_algo == 3:
    #     fringe.append([figlio.set_heuristic(goal[0]), figlio])
    # if type_algo == 4:
    #     fringe.append([padre.pathCost + costo + figlio.set_heuristic(goal[0]), figlio])




















    # if zero[0] + 1 < x:
    #
    #     for i in range(0, len(visitati)):
    #         #Vedo se il nodo è presente in visited e se la profondità è <=
    #
    #         if visitati[i].state[0] == set_state(padre.state, 3, [zero[0] + 1,zero[1]])[0] and visitati[i].depth <= padre.depth + 1:
    #             found = True
    #             break
    #     if found == False:
    #         # Verifico il costo per raggiungere il nodo
    #         costo = verifica_costi(padre, costi)
    #         # Creo il nodo e inserisco in una variaabile la distanza dal goal
    #
    #         son = Node(padre.pathCost + costo, set_state(padre.state, 3, [zero[0] + 1,zero[1]]), padre, padre.depth + 1)
    #         # Memorizzo il nodo che le informazioni necessarie nella coda
    #         coda(fringe, son, algo, padre, costo, goal)
    #     else:
    #         found = False
    #
    #         #Todo: Aggiustare gli altri tre in base al primo
    #
    # # Verifico se posso andare sopra
    # if zero[0] - 1 >= 0:
    #
    #     for i in range(0, len(visitati)):
    #         #print(set_state(padre.state, -3, [zero[0] - 1,zero[1]])[1])
    #         if visitati[i].state[0] == set_state(padre.state, -3, [zero[0] - 1,zero[1]])[0] and visitati[i].depth <= padre.depth + 1:
    #             found = True
    #             break
    #     if found == False:
    #         # Verifico il costo per raggiungere il nodo
    #         costo = verifica_costi(padre, costi)
    #         # Creo il nodo e inserisco in una variaabile la distanza dal goal
    #
    #         son = Node(padre.pathCost + costo, set_state(padre.state, -3, [zero[0] - 1,zero[1]]), padre, padre.depth +1)
    #         # Memorizzo il nodo che le informazioni necessarie nella coda
    #         coda(fringe, son, algo, padre, costo, goal)
    #     else:
    #         found = False
    #
    # # Verifico se posso andare a destra
    # if zero[1] + 1 < y:
    #
    #     for i in range(0, len(visitati)):
    #         if visitati[i].state[0] == set_state(padre.state, 1, [zero[0],zero[1] + 1])[0] and visitati[i].depth <= padre.depth + 1:
    #             found = True
    #             break
    #
    #     if found == False:
    #         # Verifico il costo per raggiungere il nodo
    #         costo = verifica_costi(padre, costi)
    #         # Creo il nodo e inserisco in una variaabile la distanza dal goal
    #
    #         son = Node(padre.pathCost + costo, set_state(padre.state, 1, [zero[0],zero[1] + 1]), padre, padre.depth +1)
    #         # Memorizzo il nodo che le informazioni necessarie nella coda
    #         coda(fringe, son, algo, padre, costo, goal)
    #     else:
    #         found = False
    #
    # # Verifico se posso andare a sinistra
    # if zero[1] - 1 >= 0:
    #
    #     # Verifico se ottengo uno stato stato già analizzato in precedenza
    #     for i in range(0, len(visitati)):
    #         if visitati[i].state[0] == set_state(padre.state, -1, [zero[0],zero[1] - 1])[0] and visitati[i].depth <= padre.depth + 1:
    #             found = True
    #             break
    #     # Se il nodo non è mai stato visitato in precedenza lo aggiungo alla coda
    #     if found == False:
    #         # Verifico il costo per raggiungere il nodo
    #         costo = verifica_costi(padre, costi)
    #         # Creo il nodo e inserisco in una variaabile la distanza dal goal
    #
    #         son = Node(padre.pathCost + costo, set_state(padre.state, -1, [zero[0],zero[1] - 1]), padre, padre.depth +1)
    #         #Memorizzo il nodo che le informazioni necessarie nella coda
    #         coda(fringe, son, algo, padre, costo, goal)
    #     else:
    #         found = False

def verifica_costi(nodo, costi):
    for i in range(0, len(costi)):
        if costi[i][0] == nodo.state[0] and costi[i][1] == nodo.state[1]:
            return costi[i][2]

    #Se non ho trovato le coordinate del nodo nella lista costi, significa che il costo è 1 e quindi restituisco 1
    return 1

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











def print_puzzle(nodo,goal):
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














