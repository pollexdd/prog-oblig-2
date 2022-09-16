pakkeliste = []

while True:

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
        print("Da er du ferdig med å pakke dette har du tatt med deg " + str(pakkeliste))
        break
        

    if valg_av_modus == "1":
        print("du har valgt pc, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til, 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("pc")
        if valg == "2":
            pakkeliste.remove("pc")

    if valg_av_modus == "2":
        print("du har valgt klær, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("klær")
        if valg == "2":
            pakkeliste.remove("klær")

    if valg_av_modus == "3":
        print("du har valgt sengetøy, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("sengetøy")
        if valg == "2":
            pakkeliste.remove("sengetøy")

    if valg_av_modus == "4":
        print("du har valgt tannbørste, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("tannbørste")
        if valg == "2":
            pakkeliste.remove("tannbørste")
    
    if valg_av_modus == "5":
        print("du har valgt kontor stol, velg hva du vil gjøre")
        valg = input("velg 1 får å legge til 2 for å slette fra liste ")
        print("1 legg til")
        print("2 slett")
        if valg == "1": 
            pakkeliste.append("kontor stol")
        if valg == "2":
            pakkeliste.remove("kontor stol")
    

    
