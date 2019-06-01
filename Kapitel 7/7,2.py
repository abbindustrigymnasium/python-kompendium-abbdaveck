import random

randomnummer = random.randint(0,99) #randint slumar ett nummer
gissningar = 1

print("Skriv in ett nummer")
nummer = int(input())

while nummer != randomnummer:   #koden under körs om input nummret inte matchar det slumpade nummret
    if nummer < randomnummer:   #om det är större:
        print("HIGHER")
        print("Skriv in ett nytt nummer")
        nummer = int(input())
        gissningar += 1 #lägger till en gissning varje gång en nytt nummer har testats
    else:
        print("LOWER")
        print("Skriv in ett nytt nummer")
        nummer = int(input())
        gissningar += 1

print("Grattis du hittade rätt nummer!")
print("Det tog", gissningar, "gissningar!")