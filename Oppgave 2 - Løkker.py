#fikk hjelp fra https://www.w3schools.com/python/python_for_loops.asp og https://www.w3schools.com/python/python_while_loops.asp

print("1 while løkke")
print("2 for løkke")

#velger om det skal være while eller for loops
valg_av_modus = input("velg modus ")
start_tall = 9

#hvis start tall er mindre en 103 blir det lagt til 2 hver gang det blir printet ut til det blir 101
if valg_av_modus == ("1"):
    while start_tall < 103:
        print(start_tall)
        start_tall += 2    

#start tall er i en for loop fra 9 til 103 og intevallen er 2 så den kjører til den når 101
if valg_av_modus == ("2"):
    for start_tall in range (9, 103, 2):
        print(start_tall)