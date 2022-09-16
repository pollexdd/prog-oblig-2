
from random import randrange
import string

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
print("velg hvor mange spillere mellom 1-4")

spillere = input("velg et tall mellom 1-4 ") 

if spillere == ("1"):
    poeng_pil_1 = randrange(0, 60)
    poeng_pil_2 = randrange(0, 60)
    poeng_pil_3 = randrange(0, 60)
    print(poeng_pil_1+poeng_pil_2+poeng_pil_3)

if spillere == ("2"):
    for poeng_pil in range (3):
        sum1 += randrange(0, 60)
        print("spiller 1 fikk " + str(sum1))
        continue
    for poeng_pil in range (3):
        sum2 += randrange(0, 60)
        print(sum2)
