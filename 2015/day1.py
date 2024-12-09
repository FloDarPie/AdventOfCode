file = open('day1input.txt', 'r')
content = file.read()
file.close()

def fonction(file):
    cpt = 0
    position = 0
    for letter in file:
        position+=1
        if letter == '(':
            cpt+=1
        elif letter == ')':
            cpt-=1
        if cpt == -1:
            print(position)
        
        
    return cpt

print(fonction(content))