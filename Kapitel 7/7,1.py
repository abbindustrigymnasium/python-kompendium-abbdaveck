print("Skriv in ett tal tal under 20")
tal = int(input())
print("Bra val!")
gånger = int(1)

while gånger < 4:   #under tiden gånger är mindre är 4:
    print(tal*gånger)
    gånger += 1

print("Vill du ha tre tal till?")
jaellernej = input()
if jaellernej == "Ja":  #om du skriver "Ja"
    while gånger < 7:
        print(tal*gånger)
        gånger += 1
    print("Vill du ha tre tal till?")
    jaellernej2 = input()
    if jaellernej2 == "Ja":
        while gånger < 10:
            print(tal*gånger)
            gånger += 1
        print("Vill du ha tre tal till?")
        jaellernej2 = input()
        if jaellernej2 == "Ja":
            while gånger < 10:
                print(tal*gånger)
                gånger += 1
            print("Vill du ha tre tal till?")
            jaellernej3 = input()
            if jaellernej3 == "Ja":
                while gånger < 13:
                    print(tal*gånger)
                    gånger += 1
        else:
            print("Okej, ha en bra dag!")
    else:
        print("Okej, ha en bra dag!")
else:
    print("Okej, ha en bra dag!")