file = open('day2input.txt', 'r')
content = file.read()
file.close()

def fonction_paper(file):
    doc = file.split("\n")
    total = 0
    for operation in doc[:-1]:
        l,w,h = operation.split('x')
        total += 2*int(l)*int(w) + 2*int(w)*int(h) + 2*int(h)*int(l) + min(int(l)*int(w) ,int(w)*int(h),int(h)*int(l))
    return total

def fonction_ribbon(file):
    doc = file.split("\n")
    total = 0
    for operation in doc[:-1]:
        value =[int(i) for i in operation.split('x')]
        value.sort()
        l,w,h = value[0], value[1], value[2]
        total += 2*(l) + 2*(w) + (l)*(w)*(h)
    return total
   
#content = "1x1x10\n"
print(fonction_paper(content))
print(fonction_ribbon(content))