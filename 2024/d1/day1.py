file = open('day1input.txt', 'r')
content = file.read()
file.close()




def fonction_1(file):
    listeA = []
    listeB = []
    for ligne in file.split("\n")[:-1]:
        a = ligne.split("   ")
        listeA.append(int(a[0]))
        listeB.append(int(a[1]))
    listeA.sort()
    listeB.sort()

    sum = 0
    for i in range(len(listeB)):
        sum += abs(listeA[i] - listeB[i])
    return sum

def fonction_2(file):
    listeA = []
    listeB = []
    for ligne in file.split("\n")[:-1]:
        a = ligne.split("   ")
        listeA.append(int(a[0]))
        listeB.append(int(a[1]))

    sum = 0
    for nombre in listeA:
        sum += nombre * listeB.count(nombre)
    return sum

print(fonction_1(content))
print(fonction_2(content))