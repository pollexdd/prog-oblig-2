
from random import randrange
import string
poeng_pil = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
print("velg hvor mange spillere mellom 1-4")

spillere = input("velg et tall mellom 1-4 ") 
#1 spiller
if spillere == ("1"):
    for poeng_pil in range (0, 3):
        sum1 += randrange(0, 60)
        continue
    print("spiller 1 fikk " + str(sum1) + " poeng.")

#2 spillere
if spillere == ("2"):
    for poeng_pil in range (0, 3):
        sum1 += randrange(0, 60)
        continue
    print("spiller 1 fikk " + str(sum1) + " poeng.")
    
    for poeng_pil in range (0, 3):
        sum2 += randrange(0, 60)
        continue
    print("spiller 2 fikk " + str(sum2) + " poeng.")

#3 spillere
if spillere == ("3"):
    for poeng_pil in range (0, 3):
        sum1 += randrange(0, 60)
        continue
    print("spiller 1 fikk " + str(sum1) + " poeng.")
    
    for poeng_pil in range (0, 3):
        sum2 += randrange(0, 60)
        continue
    print("spiller 2 fikk " + str(sum2) + " poeng.")

    for poeng_pil in range (0, 3):
        sum3 += randrange(0, 60)
        continue
    print("spiller 3 fikk " + str(sum3) + " poeng.")

#4 spillere

if spillere == ("4"):
    for poeng_pil in range (0, 3):
        sum1 += randrange(0, 60)
        continue
    print("spiller 1 fikk " + str(sum1) + " poeng.")
    
    for poeng_pil in range (0, 3):
        sum2 += randrange(0, 60)
        continue
    print("spiller 2 fikk " + str(sum2) + " poeng.")

    for poeng_pil in range (0, 3):
        sum3 += randrange(0, 60)
        continue
    print("spiller 3 fikk " + str(sum3) + " poeng.")

    for poeng_pil in range (0, 3):
        sum4 += randrange(0, 60)
        continue
    print("spiller 4 fikk " + str(sum4) + " poeng.")