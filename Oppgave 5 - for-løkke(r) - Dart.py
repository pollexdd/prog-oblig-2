from random import randrange

poeng_pil = randrange(0, 60)

print("velg hvor mange spillere mellom 1-4")

spillere = input("velg et tall mellom 1-4 ") 

if spillere == ("1"):
    poeng_pil_1 = randrange(0, 60)
    poeng_pil_2 = randrange(0, 60)
    poeng_pil_3 = randrange(0, 60)
    print(poeng_pil_1+poeng_pil_2+poeng_pil_3)

if spillere == ("2"):
    for poeng_pil in range (3):
        poeng = randrange(0, 60)
        print(poeng)