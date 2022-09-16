bøker = ["The Hobbit", "Farmer Giles of Ham", "The Fellowship of the Ring", "The Two Towers","The Return of the King" ,"The Adventures of Tom Bombadil" , "Tree and Leaf"]

# printer de 2 første bøkene i listen
print(bøker[0:2]) 
# printer de 2 siste bøkene i listen
print(bøker[5:7]) 

#legger til bøker i listen
bøker.append("The Silmarillion") 
bøker.append("Unfinished Tales")
# endrer på listen så bøkene i lotr får "lord of the rings" foran seg.
bøker[2] ="Lord of the Rings The Fellowship of the Ring"
bøker[3] ="Lord of the Rings The Two Towers"
bøker[4] ="Lord of the Rings The Return of the King"

#sorterer bøkene alfabetisk siden det ikke sto i oppgaven hvordan det skulle sortetes
bøker.sort()
print(bøker)
