import re

file = open('day3input.txt', 'r')
content = file.read()
file.close()


def fonction_1(texte):
    result = re.findall("mul\([0-9]+?,[0-9]+?\)", texte)
    resultat = 0

    for block in result:
        v = re.findall("[0-9]+", block)
        resultat += int(v[0])*int(v[1])
    return resultat


def fonction_2(texte):
    result = re.findall("do\(\)|don't\(\)|mul\([0-9]+?,[0-9]+?\)", texte)
    resultat = 0
    flag = True

    for block in result:
        if block=="do()":
            flag = True
        elif block == "don't()":
            flag = False
        elif flag:    
            v = re.findall("[0-9]+", block)
            resultat += int(v[0])*int(v[1])

    return resultat



print(fonction_1(content))
print(fonction_2(content))