print("Var bor du")
land = input()
Norden = ["Sverige", "sverige", "Norge", "norge", "Finland", "finland", "Danmark", "danmark", "Island", "island"]
Storbritanien = ["England", "england", "Wales", "wales", "Nordirland", "nordirland", "Skottland", "skottland"]

if land in Norden:  #om din input är finns i listan norden:
    print("Du bor i Norden")
else:
    if land in Storbritanien:
        print("Du bor i Storbritanien")
    else:   #om din input varken passar in på listan norden eller strbritanien får du ett elakt errormeddelande
        print("Error 404, du suger för du bor varken i Norden eller Storbritanien")