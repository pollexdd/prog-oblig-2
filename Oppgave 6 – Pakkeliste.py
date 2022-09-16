
while True:

    pakkeliste = []
    
    print("0 får å se listen")
    print("1 pc")
    print("2 klær")
    print("3 sengetøy")
    print("4 tannbørste")
    print("5 kontor stol")
    print("6 ferdig med å pakke")
    
    valg_av_modus = input("velg 0-6 ")
    

    if valg_av_modus == "0":
        print(pakkeliste)
    
    if valg_av_modus == "6":
        break
        

    if valg_av_modus == "1":
        print("du har valgt pc, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("pc")
        if valg == "2":
            pakkeliste.remove("pc")
            

    
