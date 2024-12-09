file = open('day3input.txt', 'r')
content = file.read()
file.close()

def fonction_santa(file):
    location = [0,0]
    localisation = dict()
    for i in file:
        if i=='>':
            location[0]+=1
        elif i == '<':
            location[0]-=1
        elif i=='^':
            location[1]+=1
        else:
            location[1]-=1
        localisation[str(location)] = 1
    return len(localisation)

def fonction_santa_rob(file):
    location_santa = [0,0]
    location_rob = [0,0]
    localisation = dict()
    localisation[str(location_santa)] = 1
    for i in range(1,len(file),2):
        if file[i]=='>':
            location_santa[0]+=1
        elif file[i] == '<':
            location_santa[0]-=1
        elif file[i]=='^':
            location_santa[1]+=1
        else:
            location_santa[1]-=1
        localisation[str(location_santa)] = 1

    for i in range(0,len(file),2):
        if file[i] =='>':
            location_rob[0]+=1
        elif file[i] == '<':
            location_rob[0]-=1
        elif file[i] =='^':
            location_rob[1]+=1
        else:
            location_rob[1]-=1
        localisation[str(location_rob)] = 1
    return len(localisation)


print(fonction_santa(content))
print(fonction_santa_rob(content))