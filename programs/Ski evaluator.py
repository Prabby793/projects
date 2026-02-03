import numpy

g = []

def dist(a,b):
    distsquared = 0
    for n in range(len(a)):
        distsquared += (int(a[n]) - int(b[n]))**2
    distance = numpy.sqrt(distsquared)
    return distance

def another_ski():
    x = input("Do you have another ski to compare? ")
    if x.capitalize() == "NO".capitalize():
        y = False
    else: 
        y = True
    return y


class skis:
    def __init__(self, name, width, stiffness, weight, price):
        self.name = name
        self.width = (int(width)-80)*2.5
        self.stiffness = int(stiffness)*10
        self.weight = int(weight)*10
        self.price = price

while another_ski():
    width = input("What is the ski width?, (80-120)? ")
    stiffness = input("Is the ski stiff (1-10)? ")
    weight = input("What is the ski's weight (1-10)? ")
    price = input("What is the price? ")
    name = input("What is the name? ")
    name = skis(name,width,stiffness, weight, price)
    print(name.width)
    g.append(name)

def decision(g):
    width = input("In your ideal ski, what is the ski width (80-120)? ")
    stiffness = input("What is your ideal ski stiffness (1-10)? ")
    weight = input("What is your ideal ski weight (1-10)? ")
    ideal = skis("ideal", width, stiffness, weight, 500)
    for n in g:
        if float(n.price)*0.8 >= 600:
            g.remove(n)
    choice = g[0]
    for n in g:
        if dist([choice.width,choice.stiffness,choice.weight],[ideal.width,ideal.stiffness, ideal.weight]) > dist([n.width,n.stiffness,n.weight],[ideal.width,ideal.stiffness,ideal.weight]):
            choice = n
    return choice.name


print(decision(g))