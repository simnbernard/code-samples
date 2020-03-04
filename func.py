def sayHello(name="world"):
    print("Hello {0} !".format(name))

sayHello()


def sayHello(name="world"):
    return "Hello " + name + " !"

print(sayHello())

carre = lambda x: x * x

carre(2)

multi = lambda x,y: x * y

multi(2, 3)