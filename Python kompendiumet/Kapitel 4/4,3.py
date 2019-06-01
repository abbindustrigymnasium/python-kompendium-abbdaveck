registrerade =["Anna", "Eva", " Erik", "Lars", "Karl"]
avanmälningar =["Anna", "Erik", "Karl"]

for person in avanmälningar:
    #for namnbort in avanmälningar:    
        #del registrerade[namnbort]    
        #del registrerade[registrerade.index(namnbort)]
    registrerade.remove(person) #tar bort personerna i listan avanmälningar
print (registrerade)