
import random
gånger = 0

Partier=[
    {"namn":"Socialdemokraterna","block":"Rödgröna","inriktning": "Vänster","röster": 0},
    {"namn":"Moderaterna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Sverigedemokraterna","block":"Inget","inriktning": "Höger","röster": 0},
    {"namn":"Centerpartiet","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Vänsterpartiet","block":"Rödgröna","inriktning": "Vänster","röster": 0},
    {"namn":"Kristdemokraterna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Liberalderna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Miljöpartiet","block":"Rödgröna","inriktning": "Vänster","röster": 0}
]

while gånger < 100:
    gånger += 1 
    nummer = random.randint(1,100)
    if nummer > 28:
        if nummer >48:
            if nummer >68:
                if nummer >76:
                    if nummer >84:
                        if nummer >90:
                            if nummer > 95:
                                Partier[7]["röster"] += 1
                            else:
                                Partier[6]["röster"] += 1
                        else:
                            Partier[5]["röster"] += 1
                    else:
                        Partier[4]["röster"] += 1
                else:
                    Partier[3]["röster"] += 1
            else:
                Partier[2]["röster"] += 1
        else:
            Partier[1]["röster"] += 1
    else:
        Partier[0]["röster"] += 1

tabortpartier = []

for j in range(0,len(Partier)):
    for i in range(0,len(Partier)):
        if Partier[i]["röster"] < 4:
            tabortpartier.append(Partier[i])
            del Partier[i]
            break

Rödgröna = 0
Alliansen = 0

for Parti in Partier:
    if Parti["namn"] == "Sverigedemokraterna":
        SD = Parti["röster"]
    
    if Parti["block"] == "Rödgröna":
        Rödgröna += Parti["röster"]
    
    if Parti["block"] == "Alliansen":
        Alliansen += Parti["röster"]

if Rödgröna > Alliansen:
    print("De Rödgröna bildar regering med", Rödgröna, "% av rösterna")
    print("Alliansen förlorade med", Alliansen, "% av rösterna")
    print("Sist kom Sverigedemokraterna utan block med", SD, "% av procent rösterna")
else:
    print("Alliansen bildar regering med", Alliansen, "% av rösterna")
    print("De rödgröna förlorade med", Rödgröna, "% av rösterna")
    print("Sist kom Sverigedemokraterna utan block med", SD, "% av procent rösterna")

# print("Socialdemokraterna fick ", Partier[0]["röster"],"% av rösterna")
# print("Moderaterna fick ", Partier[1]["röster"],"% av rösterna")
# print("Sverigedemokraterna fick ", Partier[2]["röster"],"% av rösterna")
# print("Centerpartiet fick ", Partier[3]["röster"],"% av rösterna")
# print("Vänsterpartiet fick ", Partier[4]["röster"],"% av rösterna")
# print("Kristdemokraterna fick ", Partier[5]["röster"],"% av rösterna")
# print("Liberalerna fick ", Partier[6]["röster"],"% av rösterna")
# print("Miljöpartiet fick ", Partier[7]["röster"],"% av rösterna")

for i in range(0,len(Partier)):
    print(Partier[i]["namn"], "fick ", Partier[i]["röster"],"% av rösterna")

for i in tabortpartier:
    print(i["namn"],"togs bort för de fick bara", i["röster"],"% av rösterna")