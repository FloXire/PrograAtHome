labyrinthe=[[1,1,1,1,1,1,1,1,1,1], \
            [1,3,1,0,0,0,0,0,0,1], \
            [1,0,1,1,1,1,0,1,0,1], \
            [1,0,0,0,1,1,0,1,0,1], \
            [1,0,1,1,1,1,0,1,0,1], \
            [1,0,1,0,1,1,0,1,0,2], \
            [1,0,1,0,0,0,0,1,1,1], \
            [1,0,1,0,1,1,0,0,0,1], \
            [1,0,0,0,1,1,0,1,0,1], \
            [1,1,1,1,1,1,1,1,1,1]]

def trajet(labyrinthe):

    placePerso = (1,1)
    trajet = []
    global victoire
    victoire = False
    
    def sortie(labyrinthe, placePerso, trajet):
        global victoire
        print(victoire)
        if placePerso in trajet:
            return
        if labyrinthe[placePerso[0]][placePerso[1]] == 2:
            print("c'est gagné")
            victoire = True
            return

        trajet.append(placePerso)
        
        listeNextMovePossib = [] #liste de coord des mouvements possibles au prochain coup
        if labyrinthe[placePerso[0]-1][placePerso[1]] in (0,2): #en haut
            listeNextMovePossib.append((placePerso[0]-1, placePerso[1]))
        if labyrinthe[placePerso[0]+1][placePerso[1]] in (0,2): #en bas
            listeNextMovePossib.append((placePerso[0]+1, placePerso[1]))
        if labyrinthe[placePerso[0]][placePerso[1]-1] in (0,2): #a gauche
            listeNextMovePossib.append((placePerso[0], placePerso[1]-1))
        if labyrinthe[placePerso[0]][placePerso[1]+1] in (0,2): #a droite
            listeNextMovePossib.append((placePerso[0], placePerso[1]+1))

        for i in range(len(listeNextMovePossib)):
            if victoire:
                return
            sortie(labyrinthe, listeNextMovePossib[i], trajet)
            

    sortie(labyrinthe, placePerso, trajet)

trajet(labyrinthe)
