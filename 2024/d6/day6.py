file = open('day6input.txt', 'r')
content = file.read()
file.close()



def fonction_1(data):

    labyrinthe = data.split("\n")[:-1]

    x = 0
    y = 0
    pointeur = 'x'
    longueur = len(labyrinthe)
    largeur = len(labyrinthe[0])

    for i in range(longueur):
        for j in range(largeur):
            if labyrinthe[i][j] == '^':
                y = int(i)
                x = int(j)
                pointeur = '^'
                break
        if x != 0 and y != 0:
            break
    #print(labyrinthe[y][x])
    #print(f"x - y : {x} - {y}")
    
    # balade in labyrinthe
    coordonnes = set()
    while -1 < x < longueur and -1 < y < largeur :
        #print(x,y, pointeur, len(coordonnes))
        if pointeur == '^':
            if labyrinthe[y-1][x] == '#':
                pointeur = '>'
            else:
                y-=1
                coordonnes.add((x,y))
        
        elif pointeur == '>':
            if labyrinthe[y][x+1] == '#':
                pointeur = 'd'
            else:
                x+=1
                coordonnes.add((x,y))

        elif pointeur == 'd':
            if labyrinthe[y+1][x] == '#':
                pointeur = '<'
            else:
                y+=1
                coordonnes.add((x,y))

        elif pointeur == '<':
            if labyrinthe[y][x-1] == '#':
                pointeur = '^'
            else:
                x-=1
                coordonnes.add((x,y))
        
            
    return len(coordonnes)


# ajout d'un élément en supprimant le premier
def avance(liste, coord):
    return liste[1:] + [coord]

def fonction_1_prime(labyrinthe, debut):

    x = debut[0]
    y = debut[1]
    pointeur = '^'
    longueur = len(labyrinthe)
    largeur = len(labyrinthe[0])


    liste_boucle = set()
   
    # balade in labyrinthe
    coordonnes = set()
    a = 0
    while -1 < x < longueur and -1 < y < largeur :
        #print(liste_boucle, a)
        a+=1
        #boucle trouvé
        if pointeur == '^':
            if y-1 ==-1:
                    return 0
            if labyrinthe[y-1][x] == '#':
                #print(">", end="")
                pointeur = '>'
                if (x,y) in liste_boucle:
                    return 1
                liste_boucle.add((x,y))
            else:
                y-=1
                coordonnes.add((x,y))
        
        elif pointeur == '>':
            if x+1 == longueur:
                    return 0
            if labyrinthe[y][x+1] == '#':
                #print("d", end="")
                pointeur = 'd'
                if (x,y) in liste_boucle:
                    return 1
                liste_boucle.add((x,y))
            else:
                x+=1
                coordonnes.add((x,y))

        elif pointeur == 'd':
            if y+1 == largeur:
                    return 0
            if labyrinthe[y+1][x] == '#':
                #print("<", end="")
                pointeur = '<'
                if (x,y) in liste_boucle:
                    return 1
                liste_boucle.add((x,y))
            else:
                y+=1
                coordonnes.add((x,y))

        elif pointeur == '<':
            if x-1 ==-1:
                    return 0
            if labyrinthe[y][x-1] == '#':
                #print("^", end="")
                pointeur = '^'
                if (x,y) in liste_boucle:
                    return 1
                liste_boucle.add((x-1,y))
            else:
                x-=1
                coordonnes.add((x,y))
    # pas de boucle trouvé       
    return 0


"""
def ajout(dico,origine, coord):
    try:
        dico[origine].append(coord)
    except:
        dico[origine] = [coord]




    
def recherche_boucle(coord,debut, lab):

    cpt = 0

    dernier_pas = [(0,0), (0,0), (0,0), (0,0)]

    test = debut
    key = debut
    index = 0
    #brute force
    while test != (-1, 76):

        # parcours du chemin
        promene = debut
        while True:
            nouveau_pas = avance(dernier_pas, promene)
            #boucle
            if set(dernier_pas) == set(nouveau_pas):
                #changement de test
                cpt +=1
                break
            try:
                promene = coord[promene][-1]
                a = coord[promene] != []
            except:
                break

        
        # chgt de test        
        index += 1
        if index == len(coord[key]):
            key = coord[key][-1]
            index = 0
        test = coord[key][index]
        print(test)
        pass

    pass

    return cpt
"""

def fonction_2(data):

    #data analysis
    labyrinthe = [[i for i in ligne] for ligne in data.split("\n")[:-1]]

    #FIND STARTER
    x = 0
    y = 0
    pointeur = 'x'
    longueur = len(labyrinthe)
    largeur = len(labyrinthe[0])

    for i in range(longueur):
        for j in range(largeur):
            if labyrinthe[i][j] == '^':
                y = int(i)
                x = int(j)
                pointeur = '^'
                break
        if x != 0 and y != 0:
            break
    origine = (x,y)
    
    # Ensemble des coordonnées du chemin du garde
    coordonnes = set()
    while -1 < x < longueur and -1 < y < largeur :
        if pointeur == '^':
            if labyrinthe[y-1][x] == '#':
                pointeur = '>'
            else:
                y-=1
                coordonnes.add((x,y))
        
        elif pointeur == '>':
            if labyrinthe[y][x+1] == '#':
                pointeur = 'd'
            else:
                x+=1
                coordonnes.add((x,y))

        elif pointeur == 'd':
            if labyrinthe[y+1][x] == '#':
                pointeur = '<'
            else:
                y+=1
                coordonnes.add((x,y))

        elif pointeur == '<':
            if labyrinthe[y][x-1] == '#':
                pointeur = '^'
            else:
                x-=1
                coordonnes.add((x,y))
    

    #les tests
    nb = 0
    for test in coordonnes:
        #print(test)
        labyrinthe[test[0]][test[1]] = "#"
        nb += fonction_1_prime(labyrinthe, origine)
        labyrinthe[test[0]][test[1]] = "."
        
    return nb


print(fonction_1(content))
print(fonction_2(content))
