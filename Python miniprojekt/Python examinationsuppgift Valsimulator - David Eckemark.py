
import random   #importerar funktionen random
gånger = 0  #deffinierar vaiabeln gånger till 0, gånger används för att se till att jag kan köra en while loop exakt 100 gånger

Partier=[   #jag gör en lista med alla partier, deras block, inrikting och en varabel för deras röster, Jag lät Partierna vara med i sitt block som de var innan Riksdagsvalet 2018 då den situationen är lite komplcerad nu 
    {"namn":"Socialdemokraterna","block":"Rödgröna","inriktning": "Vänster","röster": 0},
    {"namn":"Moderaterna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Sverigedemokraterna","block":"Inget","inriktning": "Höger","röster": 0},
    {"namn":"Centerpartiet","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Vänsterpartiet","block":"Rödgröna","inriktning": "Vänster","röster": 0},
    {"namn":"Kristdemokraterna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Liberalderna","block":"Alliansen","inriktning": "Höger","röster": 0},
    {"namn":"Miljöpartiet","block":"Rödgröna","inriktning": "Vänster","röster": 0}
]

while gånger < 100: #denna while loop kommer köras 100 gånger eftersom att varje gång jag kör den lägger jag till 1 till varablen gånger
    #Jag har gjort så varje parti har en lucka med en fast "storlek" och om det slumpade nummret hamnar i den luckan lägger jag till 1 till deras röster. 
    #det går jämföra det med en 8 sidig tärning som jag slår 100 gångar och räknar antalet gånger som varje sida kommer upp. Men jag har "riggat"
    #tärningen så chansen att Socialdemokraterna får en röst är större än chansen att Miljöpartiet får en röst. Detta gjorde jag genom att göra "luckan"
    #större för de större partierna. Jag baserade min "storlek" på luckan på resultatet i det senaste riksdagsvalet
    gånger += 1    #lägger till 1 på gånger för att koden ska köras 100 gånger
    nummer = random.randint(1,100)  #slumpar ett nummer mellan 1 och 100
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

tabortpartier = [] #gör en lista för partierna jag ska ta bort, den är tom i början men jag använder append för att lägga till de partierna som ska bort

for j in range(0,len(Partier)):     #jag har en varierande andra värde i range för antalet partier kan variera om något tas bort
    for i in range(0,len(Partier)):
        if Partier[i]["röster"] < 4:    #kollar i listan om något parti har mindre än 4 i deras röster-värde
            tabortpartier.append(Partier[i])    #då lägger jag till de i listan tabortpartier för att om jag bara tog bort dem skulle jag inte kunna visa deras röster och så vidare
            del Partier[i]  #här tar jag bort dem från listan Partier
            break #avslutar for loopen

Rödgröna = 0
Alliansen = 0

for Parti in Partier:   #här tar jag röstarna Sverigedemokraterna hade och lägger in dem i en variabel som heter SD, de har en egen for loop då de är de enda i Riksdagen utan block
    if Parti["namn"] == "Sverigedemokraterna":
        SD = Parti["röster"]
    
    if Parti["block"] == "Rödgröna":    #gör samma sak fast för alla partier som har "Rödgröna" i sin kategori för r"block"
        Rödgröna += Parti["röster"]
    
    if Parti["block"] == "Alliansen":   #samma sak för alliansen
        Alliansen += Parti["röster"]

if Rödgröna > Alliansen:    #om rödgrönas röster är fler än Alliansen:
    print("De Rödgröna bildar regering med", Rödgröna, "% av rösterna") #här har jag användning av mina variabler för antalet röster som jag gjorde tidigare
    print("Alliansen förlorade med", Alliansen, "% av rösterna")
    print("Sist kom Sverigedemokraterna utan block med", SD, "% av procent rösterna")
else:   #om det inte är så
    print("Alliansen bildar regering med", Alliansen, "% av rösterna")
    print("De rödgröna förlorade med", Rödgröna, "% av rösterna")
    print("Sist kom Sverigedemokraterna utan block med", SD, "% av procent rösterna")

for i in range(0,len(Partier)):
    print(Partier[i]["namn"], "fick ", Partier[i]["röster"],"% av rösterna")

for i in tabortpartier:
    #Här visar jag om något parti åkte ut ur riksdagen på grund av 4% spärren. Detta var lite komplicerat då om jag bara tog bort dem från Partier listan skulle jag inte kunna använda dem här.
    #Så jag la till dem i listan tabortpartier och skriver ut allt i den listan och om något parti ligger där betyder de att de har åkt ut. 
    print(i["namn"],"togs bort för de fick bara", i["röster"],"% av rösterna")