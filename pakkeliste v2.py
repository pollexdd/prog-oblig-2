#tom pakkeliste utenfor while loppen så de blir lagret
pakkeliste = []

#while loop som kjører hele tiden
while True:
    print("velg 0 får å printe liste")
    print("velg 1 får å legge til liste")
    print("velg 2 får å slette fra liste")
    print("velg 4 når du er ferdig med å pakkelisten")

    objekt = ""

    valg_av_modus = input("velg 0-3 ")
    
    #hvis man velger 0 printes listen ut
    if valg_av_modus == "0":
        print(pakkeliste)
    
    #hvis man velger 3 blir while loopen avsluttet
    if valg_av_modus == "4":
        print("Da er du ferdig med å pakke dette har du tatt med deg " + str(pakkeliste))
        break

    if valg_av_modus == "1":
        objekt = input("hva vil du legge til? ")
        pakkeliste.append (objekt)
    
    if valg_av_modus == "2":
        objekt = input("hva vil du slette? ")
        print(pakkeliste)
        pakkeliste.remove (objekt)