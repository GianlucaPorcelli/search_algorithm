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

#Funzione per verificare la presenza di muri
def verifica_muri(nodo, muri):
    if nodo.state in muri:
        return True
    else:
        return False

#Funzione per stampare il percorso ottenuto per trovare la soluzione
def print_path(nodo):
    print("Costo totale: ", nodo.pathCost)
    path = []
    percorso=[]
    while nodo.parent != None:
        path.append(nodo)
        nodo = nodo.parent
    for i in range(0, len(path)):
        percorso.append(path[i].state)
        print(percorso[i])
    return percorso

def print_solution(root,path,obstacle,x,y):
    path.append(root)
    for i in range (0,x):
        for j in range (0,y):
            if [i,j] in path:
                sys.stdout.write("|I|")
                sys.stdout.write(" ")
            else:
                if [i, j] in obstacle:
                    sys.stdout.write("|O|")
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write("| |")
                    sys.stdout.write(" ")
        print(" ")

#Funzione per generare i nodi figli
def gen_figli(padre, fringe, visitati, algo, goal, x, y, muri):
    found = False

    # Verifico se posso andare giù
    if padre.state[0] + 1 < x:
        #Controllo se la destinazione è già presente in visitati
        for i in range(0,len(visitati)):
            if algo == 1:
                if visitati[i][0]  == [padre.state[0] + 1, padre.state[1]] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break

        if found == False:
            if verifica_muri(padre, muri) == False:
                #Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + 1, [padre.state[0] + 1, padre.state[1]], padre, padre.depth + 1)
                coda(fringe, son, algo, goal)
                #print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare sopra
    if padre.state[0] - 1 >= 0:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1:
                if visitati[i][0] == [padre.state[0] - 1, padre.state[1]] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break

        if found == False:
            if verifica_muri(padre, muri) == False:
                # Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + 3, [padre.state[0] - 1, padre.state[1]], padre, padre.depth + 1)
                coda(fringe, son, algo, goal)
                # print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare destra
    if padre.state[1] + 1 < y:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1:
                if visitati[i][0] == [padre.state[0], padre.state[1] + 1] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break

        if found == False:
            if verifica_muri(padre, muri) == False:
                # Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + 2, [padre.state[0], padre.state[1] + 1], padre, padre.depth + 1)
                coda(fringe, son, algo, goal)
                # print("Nodo figlio sx: ", son.state)
        else:
            found = False

    # Verifico se posso andare sinistra
    if padre.state[1] - 1 >= 0:
        # Controllo se la destinazione è già presente in visitati
        for i in range(0, len(visitati)):
            if algo == 1:
                if visitati[i][0] == [padre.state[0], padre.state[1] - 1] and visitati[i][1] < padre.depth + 1:
                    found = True
                    break

        if found == False:
            if verifica_muri(padre, muri) == False:
                # Genero il figlio e lo inserisco nella frontiera
                son = Node(padre.pathCost + 2, [padre.state[0], padre.state[1] - 1], padre, padre.depth + 1)
                coda(fringe, son, algo, goal)
                # print("Nodo figlio sx: ", son.state)
        else:
            found = False

# Funzione per memorizzare il nodo in conda
def coda(fringe, figlio, type_algo, goal):

    if type_algo == 1:
        # Inserisco nella queue
        fringe.put(figlio)
    if type_algo == 2:
        fringe.append([figlio.pathCost, figlio])
    if type_algo == 3:
        #Inserisco nella frontiera
        fringe.append([figlio.set_heuristic(goal), figlio])
    if type_algo == 4:
        fringe.append([figlio.pathCost + figlio.set_heuristic(goal), figlio])
