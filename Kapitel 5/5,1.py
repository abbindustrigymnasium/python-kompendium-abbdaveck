users = ["Daniel Radcliffe", "Rupert Grint", "Emma Watson", "Selena Gomez"]
users2 = ["Rupert Grint", "Emma Watson", "Selena Gomez"]
users3 = ["Emma Watson", "Selena Gomez"]
users4 = ["Selena Gomez"]

hår = ["Brun", "Röd"]
hår2 = ["Brun"]

öga = ["Brun", "Blå"]
öga2 = ["Brun"]

print("Skriv in ditt fulla namn")
namn = input()

print("Vad är ditt kön? (Man eller kvinna)")
kön = input()

print("Skriv in din hårfärg")
hårfärg = input()

print("Skriv in din ögonfärg")
ögonfärg = input()

if namn in users:   #om namnet  finns listan kollar den en mindre lista varje gång med ett namn som saknas
    if namn in users2:
        if namn in users3:
            if namn in users4:
                print("Du har samma namn som Selena Gomez")
            else:
                print ("Du har samma namn som Emma Watson")
        else:
            print("Du har samma namn som Rupert Grint")
    else:   #om ditt namn inte är med måste du vara kändisen som saknas i den listan
        print("Du har samma namn som Daniel Radcliffe")
else:   #om du inte har samma namn som en kändis säger den det
    print("Du har inte samma namn som någon kändis")

if kön == "Man":
    print("Du har samma kön som Daniel Radcliffe och Rupert Grint")
else:
    print("Du har samma kön som Emma Watson och Selena Gomez")

if hårfärg in hår:
    if hårfärg in hår2:
        print("Du har samma hårfärg som Daniel Radcliffe, Emma Watson och Selena Gomez")
    else:
        print("Du har samma hårfärg som Rupert Grint")
else:
    ("Du har inte samma hårfärg som någon kändis")

if ögonfärg in öga:
    if ögonfärg in öga2:
        print("Du har samma ögonfärg som Daniel Radcliffe, Emma Watson och Selena Gomez")
    else:
        print("Du har samma ögonfärg som Rupert Grint")
else:
    ("Du har inte samma ögonfärg som någon kändis")
