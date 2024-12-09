file = open('day2input.txt', 'r')
content = file.read()
file.close()


test = "7 6 4 2 1\n1 2 7 8 9\n9 7 6 2 1\n1 3 2 4 5\n8 6 4 4 1\n1 3 6 7 9\n"

def check_safe(tableau):
    if tableau[0] > tableau[1]:
        #decrease
        for i in range(len(tableau)-1):
            #error increase
            if tableau[i] <= tableau[i+1]:
                return 0
            
            #error big step
            if abs(tableau[i] - tableau[i+1]) > 3:
                return 0
        pass
    else:
        #increase
        for i in range(len(tableau)-1):
            #error decrease
            if tableau[i] >= tableau[i+1]:
                return 0
            
            #error big step
            if abs(tableau[i] - tableau[i+1]) > 3:
                return 0
        pass
    return 1

def fonction_1(file):
    somme = 0
    for ligne in file.split("\n")[:-1]:
        input = [int(i) for i in ligne.split(" ")]
        somme += check_safe(input)
        pass
    return somme

def fonction_2(file):
    somme = 0
    for ligne in file.split("\n")[:-1]:
        input = [int(i) for i in ligne.split(" ")]

        for i in range(len(input)):
            if check_safe(input[:i]+input[i+1:])==1:
                somme += 1
                break
        pass
    return somme

print(fonction_1(content))
print(fonction_2(test))
print(fonction_2(content))
