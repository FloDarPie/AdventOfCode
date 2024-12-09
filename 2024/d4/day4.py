file = open('day4input.txt', 'r')
content = file.read()
file.close()


def verif_voisin(a,b,document):

    nb = 0
    valide_bas, valide_droite, valide_gauche, valide_haut = False,False,False,False

    #verif horizontale droite
    if a+3<len(document[0]):
        valide_droite = True
        if document[a+1][b]=="M" and document[a+2][b]=="A" and document[a+3][b]=="S":
            nb+=1
    
    #verif horizontale gauche
    if a-3>-1:
        valide_gauche = True
        if document[a-1][b]=="M" and document[a-2][b]=="A" and document[a-3][b]=="S":
            nb+= 1

    #verif verticale haute
    if b-3>-1:
        valide_haut = True
        if document[a][b-1]=="M" and document[a][b-2]=="A" and document[a][b-3]=="S":
            nb+= 1

    #verif verticale basse
    if b+3<len(document):
        valide_bas = True
        if document[a][b+1]=="M" and document[a][b+2]=="A" and document[a][b+3]=="S":
            nb+= 1
    
    # diagonale droite
    if valide_droite:
        if valide_bas:
            if document[a+1][b+1]=="M" and document[a+2][b+2]=="A" and document[a+3][b+3]=="S":
                nb+= 1
        
        if valide_haut:
            if document[a+1][b-1]=="M" and document[a+2][b-2]=="A" and document[a+3][b-3]=="S":
                nb+= 1
    
    #diagonale gauche
    if valide_gauche:
        if valide_bas:
            if document[a-1][b+1]=="M" and document[a-2][b+2]=="A" and document[a-3][b+3]=="S":
                nb+= 1
        
        if valide_haut:
            if document[a-1][b-1]=="M" and document[a-2][b-2]=="A" and document[a-3][b-3]=="S":
                nb+= 1

    return nb



# recherche du motif "XMAS"
# ecrit à l'endroit
#   -   à l'envers
#   -   en diagonale
#   -   verticale
#   -   horizontale
#
def fonction_1(document):
    document = document.split("\n")[:-1]
    
    largeur = len(document[0])
    compteur = 0
    for i in range(len(document)):
        for j in range(largeur):
            if document[i][j] == 'X':
                #regarde si les voisins sont correctes
                compteur += verif_voisin(i,j,document)

            pass
        pass
    return compteur


print(fonction_1(content))



def verif_voisin_croix(a,b,document):

    #attention au débordement
    if a-1>-1 and a+1<len(document[0]) and b+1 < len(document) and b-1>-1:
        #M.S
        #.A.
        #M.S
        if document[a-1][b-1] == "M" and document[a+1][b-1] == "S" and document[a-1][b+1] == "M" and document[a+1][b+1] == "S":
            return 1
        #M.M
        #.A.
        #S.S
        elif document[a-1][b-1] == "M" and document[a+1][b-1] == "M" and document[a-1][b+1] == "S" and document[a+1][b+1] == "S":
            return 1
        #S.M
        #.A.
        #S.M
        elif document[a-1][b-1] == "S" and document[a+1][b-1] == "M" and document[a-1][b+1] == "S" and document[a+1][b+1] == "M":
            return 1
        #S.S
        #.A.
        #M.M
        elif document[a-1][b-1] == "S" and document[a+1][b-1] == "S" and document[a-1][b+1] == "M" and document[a+1][b+1] == "M":
            return 1

    return 0



# recherche du motif "MAS"
# ecrit à l'endroit
#   -   à l'envers
#   -   en diagonale
#   -   verticale
#   -   horizontale
#
def fonction_2(document):
    document = document.split("\n")[:-1]
    
    largeur = len(document[0])
    compteur = 0
    for i in range(len(document)):
        for j in range(largeur):
            if document[i][j] == 'A':
                #regarde si les voisins sont correctes
                compteur += verif_voisin_croix(i,j,document)

            pass
        pass
    return compteur



test = "MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX\n"


print(fonction_2(content))

