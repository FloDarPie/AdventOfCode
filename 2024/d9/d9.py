with open('input.txt') as file:
    content = file.read()



# give me the number of ids - order of blank
def analysis(content):
    dico = dict()
    dico[-1] = []
    id = 0
    flag = 1
    for i in content[:-1]:
        if flag:
            dico[id] = int(i)
            flag = 1 - flag
            id += 1
        else:
            flag = 1 - flag
            dico[-1].append(int(i))
        
    return dico


def compact(analyse):
    output = []
    
    #pointeur
    id = 0
    id_fin = len(analyse)-2
    blank_pointer = 0
    remplissage = 1

    while len(analyse) != 1:
        #ajout des blocks en position corrects
        if remplissage:
            output += [id] * analyse[id]
            del analyse[id]
            id+=1
            remplissage = 1 - remplissage
        
        # remplissage des blocks de fin | 1 par 1
        else:
            while analyse[-1][blank_pointer] != 0:
                analyse[-1][blank_pointer] -= 1
                output.append(id_fin)
                analyse[id_fin] -= 1
                if analyse[id_fin] == 0:
                    del analyse[id_fin]
                    id_fin -= 1
                    pass
                pass
            blank_pointer += 1
            remplissage = 1 - remplissage
            pass
        #print(f" analyse : {analyse},\n id : {id}, id_fin : {id_fin}, pointeur espace : {blank_pointer}, flag : {remplissage}")
        #print(output)
        
        pass
    return output

def compact_part2_old(analyse):
    output = []
    
    #pointeur
    id = 0
    id_fin = len(analyse)-2
    blank_pointer = 0
    remplissage = 1

    while len(analyse) != 1:
        #ajout des blocks en position corrects
        if remplissage:
            id = list(analyse.keys())[1]
            output += [id] * analyse[id]
            del analyse[id]
            remplissage = 1 - remplissage
            
        
        # remplissage des blocks de fin
        else:
            while analyse[-1][blank_pointer] != 0:
                liste = list(analyse.keys())
                for i in range(len(liste)-1, 0, -1):
                    print(i)
                    id_fin = liste[i]
                    if analyse[-1][blank_pointer] >= analyse[id_fin]:    
                        analyse[-1][blank_pointer] -= analyse[id_fin]
                        output += [id_fin] * analyse[id_fin] 
                        del analyse[id_fin]

                    # condition d'arret
                    if analyse[-1][blank_pointer] == 0:
                        remplissage = 1 - remplissage
                        break
                    elif i == 1:
                        output += [0] * analyse[-1][blank_pointer]
                        analyse[-1][blank_pointer] = 0
                        remplissage = 1 - remplissage
                pass
            blank_pointer += 1
            
            pass
        print(f" analyse : {analyse},\n id : {id}, id_fin : {id_fin}, pointeur espace : {blank_pointer}, flag : {remplissage}")
        print(output)


        #ajout des blancs
        
        pass
    return output

def modification(disk_layout, blank_pointer, id_fin, nb_file):
    #print(f"error ? : {blank_pointer}, case : {1 +2*blank_pointer}")
    #print(f"avant modif : {disk_layout[1 +2*blank_pointer]}, reduction : {nb_file}")

    new_disk_layout = []
    to_erase = [id_fin] * nb_file
    space_length = disk_layout[1 +2*blank_pointer][0]
    for i in range(len(disk_layout)):
        if i == 2*blank_pointer:
            new_disk_layout.append(disk_layout[i] + [id_fin]*nb_file)
        elif i == 2*blank_pointer+1:
            if space_length - nb_file == 0:
                new_disk_layout.append([])
            else:
                new_disk_layout.append([space_length-nb_file])
        elif disk_layout[i] == to_erase :
            new_disk_layout.append([0] * nb_file)
        else :
            new_disk_layout.append(disk_layout[i])
    
    #print(f"apres modif {new_disk_layout[1 +2*blank_pointer]}")
    return new_disk_layout

def compact_part2(analyse):
    #print(analyse)
    # Step 1: Build the initial disk layout as a list of spaces and file IDs
    disk_layout = []
    t = len(analyse)
    for idx in range(t):
        file_size = analyse.get(idx, 0)
        if file_size > 0:
            disk_layout.append([idx] * file_size)
        
        # Append the corresponding free space
        if idx == t-2:
            break
        else:
            space_size = analyse[-1][idx]
            if space_size >= 0:
                disk_layout.append([space_size])
    #print(disk_layout)

    # fix only holes
    t_blank = len(analyse[-1])
    blank_pointer = 0
    while blank_pointer != t_blank:
        print(blank_pointer)
        liste = list(analyse.keys())
        #print(f' pointeur : {blank_pointer}, memoire : {analyse[-1][blank_pointer]}, disk {disk_layout[2*blank_pointer+1]}')
        for i in range(len(liste)-1, 0, -1):
            id_fin = liste[i]
            if analyse[-1][blank_pointer] >= analyse[id_fin]:
                analyse[-1][blank_pointer] -= analyse[id_fin]
                disk_layout = modification(disk_layout, blank_pointer, id_fin, analyse[id_fin])
                del analyse[id_fin]
            
            if analyse[-1][blank_pointer] == 0 or i == 1:
                blank_pointer+=1
                break
        #print(f"blanck : {analyse[-1]}, pointeur : {blank_pointer}")
        #print(disk_layout)
    
        
    # Step 3: Return the final disk layout
    output = []
    for i in range(len(disk_layout)):
        if i%2==0:
            output += disk_layout[i]
        elif disk_layout[i] == []:
            pass
        else:
            output += [0]*disk_layout[i][0]
    return output

        
def calcul(compacted):
    somme = 0
    for i in range(len(compacted)):
        somme += i * compacted[i]
    return somme



test = "2333133121414131402\n"

a = 0
b = 1
if a:
    analyse = analysis(test)
    compacted = compact(analyse)
    print(calcul(compacted))

# -------------- CHALLENGE -------------- #

if a :
    analyse_chal = analysis(content)
    compacted = compact(analyse_chal)
    print(calcul(compacted))

################# PART 2 ##################

analyse = analysis(test)
compacted_2 = compact_part2(analyse)
print(compacted_2)
print(calcul(compacted_2))


print('\n###########################################\n')
if b :
    analyse_chal = analysis(content)
    compacted_chal_2 = compact_part2(analyse_chal)
    print(calcul(compacted_chal_2))

