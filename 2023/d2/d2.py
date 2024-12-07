#
#
#
# Format :
#
# id r v b


def analyse(ligne):
    tableau = []

    info = ligne.split(" ")
    tableau.append(int(info[1][:-1]))

    return tableau



fichier = open("inputd2.txt", "r")
for ligne in fichier:

    dico = analyse(ligne)
    print(ligne, dico)
