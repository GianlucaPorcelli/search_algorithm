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

    #Definisco l'euristica di manatthan
    def set_heuristic(self, goal):
        #Copio la lista contenente lo stato attuale del vettore in una lista ausiliaria
        aux = list(self.state[0])
        #Scompongo la lista ausiliaria in una matrice
        list1 = [[aux[0], aux[1], aux[2]], [aux[3], aux[4], aux[5]], [aux[6], aux[7], aux[8]]]
        #Copio in una seconda lista ausiliaria lo stato goal
        list2 = list(goal)

        self.heuristic = 0
        #Per ogni tessera del puzle, vado a vedere quanto è distante dalla posizione goal
        for x in range(0, 9):
            found = False
            #Visto che oltre a muovermi sia a dx che a sx posso muovermi anche verso l'alto e il basso

            for i in range(0, 3):
                for j in range(0, 3):
                    if (list1[i][j] != list2[x]):
                        # Ogni volta che la posizione goal si trova su un'altra riga della matrice,
                        # per ogni riga di distanza incremento di 1 (i), ossia i passi per raggiungere quella riga
                        # Se invece si trova a dx o sx, incremento di j
                        # Sommo con i valori precedentemente calcolati
                        self.heuristic = self.heuristic + i + j
                    else:
                        found = True
                        break
            if found == True:
                break

        return self.heuristic

    # def set_heuristic(self, goal):
    #
    #     self.heuristic = 0
    #     gol = list(goal)
    #     for i in range(0, len(self.state[0])):
    #         if self.state[0][i] != gol[i]:
    #             self.heuristic += 1
    #     return self.heuristic