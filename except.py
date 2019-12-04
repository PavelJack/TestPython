def Funct1():
    print("Start1")
    raise Exception
    print("EndF1")

def Funct2():
    print("Start2")
    Funct1()
    print("EndF2")

Funct2()