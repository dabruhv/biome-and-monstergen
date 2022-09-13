import random



def biome():
    x = random.randrange(1,4)
    if x == 1:
        print("you're in the woods")
    elif x == 2:
        print("you're under water")
    else:
        print("AHHH UR IN DA NETHER")
    monstergen(x)
def monstergen(biome):
    m = random.randrange(11)
    if biome == 1:
        if m <=3:
            print("A zombie has spawned")
        elif m < 7:
            print("A creeper has spawned")
        elif m<=8:
            print("A witch has spawned")
        else:
            print("A Skeleton has spawned")
    elif biome ==2:
        if m <=6:
            print("issa fish")
        elif m <= 8:
            print("its da dolphin")
        elif m == 9:
            print("cute axolotl")
        else:
            print("goofy ahh drowned")
        
    else:
        if m <=6:
            print("witherskeleton has spawned")
        elif m <= 8:
            print("ghast has spawned")
        elif m == 9:
            print("hoglin has spawned")
        else:
            print("blaze has spawned")
biome()

