file = open('day5input.txt', 'r')
content = file.read()
file.close()



def fonction_1(content):
    document = content.split("\n\n")
    instruction = document[0].split("\n")
    updates = [[int(j) for j in i.split(",")] for i in document[1].split("\n")[:-1]]

    memoire = dict()
    for consigne in instruction:
        try:
            memoire[int(consigne[:2])].append(int(consigne[3:]))
        except:
            memoire[int(consigne[:2])] = [int(consigne[3:])]


    value = 0
    for update in updates:    
        
        #verification validité de la consigne
        index = 0
        while index < len(update)-1 and update[index+1] in memoire[update[index]]:
            index += 1
        
        #récupération du résultat
        if index == len(update)-1:
            value += update[len(update)//2]

    return value


print(fonction_1(content))


# try to redo the arborescence between elements
# remove elements from the original list
def order(update, memory):
    ordered_update = []
    info_collecting = []
    for element in update:
        possible = []
        for suivant in update:
            if suivant in memory[element]:
                possible.append(suivant)
        info_collecting.append((element,possible))

    info2=info_collecting[:]
    while len(ordered_update) != len(update):
        v = 0
        for i in range(len(info2)):
            if info2[i][1] == []:
                v = info2[i][0]
                ordered_update = [v]+ordered_update

        to_delete=[]
        for i in range(len(info2)):
            if v in info2[i][1] :
                info_collecting[i][1].remove(v)
            if v == info2[i][0]:
                to_delete.append(i)
        for i in to_delete:
            del info_collecting[i]
        info2=info_collecting[:]

    return ordered_update


def fonction_2(content):
    document = content.split("\n\n")
    instruction = document[0].split("\n")
    updates = [[int(j) for j in i.split(",")] for i in document[1].split("\n")[:-1]]

    memoire = dict()
    for consigne in instruction:
        try:
            memoire[int(consigne[:2])].append(int(consigne[3:]))
        except:
            memoire[int(consigne[:2])] = [int(consigne[3:])]

    value = 0
    bad_updates = []
    for update in updates:    
        
        #verification validité de la consigne
        index = 0
        while index < len(update)-1 and update[index+1] in memoire[update[index]]:
            index += 1
        
        #récupération du résultat
        if index != len(update)-1:
            bad_updates.append(update)
    
    #put it in order
    for update in bad_updates:
        update = order(update, memoire)
        value += update[len(update)//2]


    return value

print(fonction_2(content))