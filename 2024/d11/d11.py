file = open('input.txt', 'r')
content = file.read()
file.close()


# starting point
#content = "125 17\n"
pluto_stones = (content.split("\n")[:-1][0]).split(" ")
print(pluto_stones)

# rules time management
# input : str
def transformation(stone):
    #print(stone)
    if stone == '0':
        stone = ['1']
    elif len(stone)%2==0:
        stone = [stone[:len(stone)//2], str(int(stone[len(stone)//2:])) ]
    else:
        stone = [str(int(stone)*2024)]
    return stone


def blink(pluto_stones):
    new_pluto_stones = []
    for stone in pluto_stones:
        new_pluto_stones += (transformation(stone))
    return new_pluto_stones

# evaluation function part2
def calculatoire(space_memory):
    total = 0
    for stone in space_memory:
        total += space_memory[stone]
    return total


def saut_temporel(pluto_stones):
    space_memory = dict()
    
    # defined space memory
    for stone in pluto_stones:
        next_stone = transformation(stone)
        #ajout nouveaux elements
        for pebble in next_stone:
            try:
                space_memory[pebble] += pluto_stones[stone]

            except:
                space_memory[pebble] = pluto_stones[stone]
        
    return space_memory


# evaluate challenge
spatial_dico = dict()

for stone in pluto_stones:
    spatial_dico[stone] = 1

for _ in range(75):
    spatial_dico = saut_temporel(spatial_dico)
print(calculatoire(spatial_dico))



