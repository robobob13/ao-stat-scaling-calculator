from math import *

max = int(input("Max Level: "))
def gbeq(stat):
    frog = (1.35*((1.44*(log(0.1*stat+4))**3+0.15*stat)/(0.1+0.15*sqrt(max))-0.79))
    return frog

while True:
    inp = int(input("Choose:\n1)Atk Size\n2)Atk Speed\n3)Resistance\n4)Regeneration\n5)Other\n"))
    if inp == 1:
        val = int(input("Atk Size: "))
        aff = float(input("Size Affinity: "))
        eqq = gbeq(val)
        final = (0.8*eqq)*((aff+3)/(aff*4))
        print(str(final))
    elif inp == 2:
        val = int(input("Atk Speed: "))
        eqq = gbeq(val)
        final = (0.4*eqq)
        print(str(final))
    elif inp == 3:
        val = int(input("Resistance: "))
        eqq = gbeq(val)
        final = (0.75*eqq)
        print(str(final))
    elif inp== 4:
        val = int(input("Regeneration: "))
        eqq = gbeq(val)
        final = (0.8*eqq)
        print(str(final))
    elif inp==5:
        val = int(input("Stat Value: "))
        eq = gbeq(val)
        print(str(eq))

    print("\n")