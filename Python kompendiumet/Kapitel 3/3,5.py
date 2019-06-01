male = [
    "Erik",
    "Lars",
    "Karl",
    "Anders",
    "Johan"
    ]

female = [
    "Maria",
    "Anna",
    "Margareta",
    "Elisabeth",
    "Eva"
    ]

print("Skriv in namnet du vil ta bort")

nameone = input()
del female[female.index(nameone)]   #tar bort det namnet som skrivs in
print(female)