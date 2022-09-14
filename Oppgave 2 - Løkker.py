#fikk hjelp fra https://www.w3schools.com/python/python_for_loops.asp og https://www.w3schools.com/python/python_while_loops.asp

print("1 while løkke")
print("2 for løkke")

valg_av_modus = input("velg modus ")

start_tall = 9
if valg_av_modus == ("1"):
    while start_tall < 103:
        print(start_tall)
        start_tall += 2    


if valg_av_modus == ("2"):
    for start_tall in range (9, 103, 2):
        print(start_tall)