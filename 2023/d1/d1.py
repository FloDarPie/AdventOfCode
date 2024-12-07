#
# Objectif : faire un code qui lit le premier chiffre
#                                  le dernier chiffre
#                                  les concatene
#                                  renvoie la somme de tous
#

def analyse(mot):
    suite=""

    #chiffre = ["one","two","three","four","five", "six", "seven","eight","nine"]

    for lettre in range(len(mot)):
        if mot[lettre].isnumeric():
            suite+=mot[lettre]
        else:
            try:
                match mot[lettre] :
                    #one
                    case "o":
                        if mot[lettre+1] == "n" and mot[lettre+2] == "e":
                            suite+="1"
                            lettre+=3
                            pass
                        pass
                    #two three
                    case "t" :
                        if mot[lettre+1]=="w" and mot[lettre+2] == "o":
                            suite+="2"
                            lettre+=3
                            pass
                        elif mot[lettre+1]=="h" and mot[lettre+2] == "r" and mot[lettre+3] == "e" and mot[lettre+4] == "e" :
                            suite+="3"
                            lettre+=5
                            pass
                        pass
                    #four five
                    case "f" :
                        if mot[lettre+1]=="o" and mot[lettre+2] == "u" and mot[lettre+3] == "r":
                            suite+="4"
                            lettre+=4
                            pass
                        elif mot[lettre+1]=="i" and mot[lettre+2] == "v" and mot[lettre+3] == "e":
                            suite+="5"
                            lettre+=4
                            pass
                        pass
                    #six seven
                    case "s" :
                        if mot[lettre+1] == "i" and mot[lettre+2] == "x":
                            suite+="6"
                            lettre+=3
                            pass
                        elif mot[lettre+1] == "e" and mot[lettre+2] == "v" and mot[lettre+3] == "e" and mot[lettre+4] == "n":
                            suite+="7"
                            lettre+=5
                            pass
                        pass

                    #eight
                    case "e" :
                        if mot[lettre+1]=="i" and mot[lettre+2] == "g" and mot[lettre+3] == "h" and mot[lettre+4] == "t" :
                            suite+="8"
                            lettre+=5
                            pass
                        pass
                    #nine
                    case "n" :
                        if mot[lettre+1]=="i" and mot[lettre+2] == "n" and mot[lettre+3] == "e":
                            suite+="9"
                            lettre+=4
                            pass
                        pass
                    case _:
                        pass
            except:
                pass
            if lettre == len(mot):
                break
            pass
        pass


    return suite


def calcul(mot):
    mot = analyse(mot)
    return int(mot[0])*10+int(mot[-1])
    a = 0
    b = 0
    flag = False
    for lettre in mot:
        if lettre.isnumeric():
            if not flag:
                a = int(lettre)
                b = int(lettre)
                flag = True
                pass
            b = int(lettre)
            pass
        pass
    return a*10+b




fichier = open("inputd1.txt", "r")

test = False
if not test:
    mot = ""
    somme = 0
    for mot in fichier:
        somme += calcul(mot[:-1])
        print(mot[:-1], analyse(mot[:-1]), calcul(mot[:-1]))
    print(somme)
else:
    mot = "mtqxjrcn1two9fourncghmnbsseight"
    print(mot)
    print(analyse(mot))

