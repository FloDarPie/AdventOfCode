file = open('input.txt', 'r')
content = file.read()
file.close()
'''
test = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732\n"
content = test
'''
splitted = content.split('\n')[:-1]
map_y = len(splitted)
map_x = len(splitted[0])

map = [[-1]*(map_x+2)] + [[-1]+[int(i) for i in j]+[-1] for j in splitted] + [[-1]*(map_x+2)]


def affichage_map(map, map_y, map_x):
    print(map[0])
    for y in range(map_y):
        print(map[y+1])
    print(map[map_y+1])


def recherche_depart(map, map_x, map_y):
    pt_dep = set()

    for y in range(1, map_y+1):
        for x in range(1, map_x+1):
            if map[y][x] == 0:
                pt_dep.add((y,x))
    return pt_dep

def parcours_chemin(map, pt_depart, value):
    print(f"---- {pt_depart} = {value}")
    # condition d'arret
    if value == 9:
        return 1
    
    y = pt_depart[0]
    x = pt_depart[1]
    total = 0
    
    # regarde au dessus
    if map[y-1][x] == value+1:
        total += parcours_chemin(map, (y-1,x), value+1)
    
    # regarde en dessous
    if map[y+1][x] == value+1:
        total += parcours_chemin(map, (y+1,x), value+1)
    
    # regarde a droite
    if map[y][x+1] == value+1:
        total += parcours_chemin(map, (y,x+1), value+1)
    
    # regarde a gauche
    if map[y][x-1] == value+1:
        total += parcours_chemin(map, (y,x-1), value+1)

    return total




def parcours_chemin_simple(map, pt_depart, value):
    global CPT, TAB
    #print(f"---- {pt_depart} = {value}")
    # condition d'arret

    if value == 9 and pt_depart not in TAB:
        TAB.add(pt_depart)
        #print(f"trouvé : {pt_depart}")
        return
    
    y = pt_depart[0]
    x = pt_depart[1]
    
    # regarde au dessus
    if map[y-1][x] == value+1:
        parcours_chemin_simple(map, (y-1,x), value+1)
    
    # regarde en dessous
    if map[y+1][x] == value+1:
         parcours_chemin_simple(map, (y+1,x), value+1)
    
    # regarde a droite
    if map[y][x+1] == value+1:
        parcours_chemin_simple(map, (y,x+1), value+1)
    
    # regarde a gauche
    if map[y][x-1] == value+1:
        parcours_chemin_simple(map, (y,x-1), value+1)


def analyse_chemin(map, pt_dep):
    global TAB
    total = 0
    for pt_depart in pt_dep:
        TAB = set()
        parcours_chemin_simple(map, pt_depart ,0)
        total += len(TAB)
        #print(f"start : {pt_depart}")
    return total

def analyse_chemin_part2(map, pt_dep):
    total = 0
    for pt_depart in pt_dep:
        total += parcours_chemin(map, pt_depart ,0)
        #print(f"start : {pt_depart}")
    return total




affichage_map(map, map_y, map_x)
pt_departs = recherche_depart(map, map_x, map_y)
print( analyse_chemin(map, pt_departs))

pt_departs = recherche_depart(map, map_x, map_y)
print(analyse_chemin_part2(map, pt_departs))