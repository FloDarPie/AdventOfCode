with open('input.txt') as file:
    content = file.read()


map = [[j for j in i] for i in content[:-1].split("\n")]


def antenne_locator(map):
    antennes = {}
    for y, ligne in enumerate(map):
        for x, signal in enumerate(ligne):
            if signal != '.':
                if signal not in antennes:
                    antennes[signal] = []
                antennes[signal].append((x, y))
    return antennes


def antinode_calculator(antennes, max_x, max_y):
    coord = set()

    for signal in antennes:
        t = len(antennes[signal])
        
        for i in range(t):
            (x1, y1) = antennes[signal][i]
            for j in range(i + 1, t):
                (x2, y2) = antennes[signal][j]
                print('\nx1, y1 :', (x1, y1))
                print('x2, y2 :', (x2, y2), end=" ")
                ajout = 0
                # horizontal
                if x1 == x2:
                    dist = abs(y2 - y1)
                    if 0 <= (min(y1, y2) - dist):
                        coord.add((x1, min(y1, y2) - dist))
                    if (max(y1, y2) + dist) < max_y:
                        coord.add((x1, max(y1, y2) + dist))
                # vertical
                elif y1 == y2:
                    dist = abs(x2 - x1)
                    if 0 <= (min(x1, x2) - dist):
                        coord.add((min(x1, x2) - dist, y2))
                    if (max(x1, x2) + dist) < max_x:
                        coord.add((max(x1, x2) + dist, y2))
                # diagonal
                else:
                    distx = abs(x2 - x1)
                    disty = abs(y2 - y1)
                    print(distx, disty)
                    
                    # Top-left to bottom-right diagonal
                    if x1 < x2 and y1 < y2:  
                        if 0 <= (x1 - distx) and 0 <= (y1 - disty):
                            coord.add((x1 - distx, y1 - disty))
                        if max_x > (x2 + distx) and max_y > (y2 + disty):
                            coord.add((x2 + distx, y2 + disty))
                    # Bottom-left to top-right diagonal
                    elif x1 < x2 and y1 > y2:
                        if 0 <= (x1 - distx) and max_y > (y1 + disty):
                            coord.add((x1 - distx, y1 + disty))
                        if max_x > (x2 + distx) and 0 <= (y2 - disty):
                            coord.add((x2 + distx, y2 - disty))
                    # Top-right to bottom-left diagonal
                    elif x1 > x2 and y1 < y2:
                        if max_x > (x1 + distx) and 0 <= (y1 - disty):
                            coord.add((x1 + distx, y1 - disty))
                        if 0 <= (x2 - distx) and max_y > (y2 + disty):
                            coord.add((x2 - distx, y2 + disty))
                    # Bottom-right to top-left diagonal
                    elif x1 > x2 and y1 > y2:
                        if max_x > (x1 + distx) and max_y > (y1 + disty):
                            coord.add((x1 + distx, y1 + disty))
                        if 0 <= (x2 - distx) and 0 <= (y2 - disty):
                            coord.add((x2 - distx, y2 - disty))

    affiche_antenne(coord, max_x, max_y)
    return len(coord)

def antinode_calculator_repetition(antennes, max_x, max_y):
    coord = set()

    for signal in antennes:
        t = len(antennes[signal])
        
        for i in range(t):
            (x1, y1) = antennes[signal][i]
            for j in range(i + 1, t):
                (x2, y2) = antennes[signal][j]
                print('\nx1, y1 :', (x1, y1))
                print('x2, y2 :', (x2, y2), end=" ")
                ajout = 0
                # horizontal
                if x1 == x2:
                    dist = abs(y2 - y1)
                    if 0 <= (min(y1, y2) - dist):
                        coord.add((x1, min(y1, y2) - dist))
                    if (max(y1, y2) + dist) < max_y:
                        coord.add((x1, max(y1, y2) + dist))
                # vertical
                elif y1 == y2:
                    dist = abs(x2 - x1)
                    if 0 <= (min(x1, x2) - dist):
                        coord.add((min(x1, x2) - dist, y2))
                    if (max(x1, x2) + dist) < max_x:
                        coord.add((max(x1, x2) + dist, y2))
                # diagonal
                else:
                    distx = 0
                    disty = 0
                    print(distx, disty)
                    distx_mem = abs(x2 - x1)
                    disty_mem = abs(y2 - y1)
                    while distx < max_x and disty < max_y:
                        # Top-left to bottom-right diagonal
                        if x1 < x2 and y1 < y2:  
                            if 0 <= (x1 - distx) and 0 <= (y1 - disty):
                                coord.add((x1 - distx, y1 - disty))
                            if max_x > (x2 + distx) and max_y > (y2 + disty):
                                coord.add((x2 + distx, y2 + disty))
                        # Bottom-left to top-right diagonal
                        elif x1 < x2 and y1 > y2:
                            if 0 <= (x1 - distx) and max_y > (y1 + disty):
                                coord.add((x1 - distx, y1 + disty))
                            if max_x > (x2 + distx) and 0 <= (y2 - disty):
                                coord.add((x2 + distx, y2 - disty))
                        # Top-right to bottom-left diagonal
                        elif x1 > x2 and y1 < y2:
                            if max_x > (x1 + distx) and 0 <= (y1 - disty):
                                coord.add((x1 + distx, y1 - disty))
                            if 0 <= (x2 - distx) and max_y > (y2 + disty):
                                coord.add((x2 - distx, y2 + disty))
                        # Bottom-right to top-left diagonal
                        elif x1 > x2 and y1 > y2:
                            if max_x > (x1 + distx) and max_y > (y1 + disty):
                                coord.add((x1 + distx, y1 + disty))
                            if 0 <= (x2 - distx) and 0 <= (y2 - disty):
                                coord.add((x2 - distx, y2 - disty))

                        #augmentation de la distance
                        distx += distx_mem
                        disty += disty_mem

    affiche_antenne(coord, max_x, max_y)
    return len(coord)


test = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]


# 0 -> 2 + 1 + 1 + 2 + 2 + 2
# A -> 2 + 1 + 2
result = [
    "......#....#",
    "...#....0...",
    "....#0....#.",
    "..#....0....",
    "....0....#..",
    ".#....A.....",
    "...#........",
    "#......#....",
    "........A...",
    ".........A..",
    "..........#.",
    "..........#.",
]
def affiche_antenne(coord, max_x, max_y):
    tableau = [['.' for _ in range(max_x)] for _ in range(max_y)]

    for c in coord:
        tableau[c[1]][c[0]] = '#'

    for ligne in tableau:
        for c in ligne:
            print(c, end='')
        print()

########################## test
max_y = len(test)
max_x = len(test[0])

antennes = antenne_locator(test)
print(antinode_calculator(antennes, max_x, max_y))
print(antinode_calculator_repetition(antennes, max_x, max_y))

########################## challenge

print('-----------------------------')

max_y = len(map)
max_x = len(map[0])

antennes = antenne_locator(map)
print(antinode_calculator(antennes, max_x, max_y))
print(antinode_calculator_repetition(antennes, max_x, max_y))



