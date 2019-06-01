print("Vill du överföra från miles till km eller tvärt om (skriv km om du vill överföra från km till miles och miles annars)")
milesellerkm = input()
print("Vilken distans?")
distance = input()

def km_to_miles (km):   #definar en funktion så när jag skriver in km_to_miles kommer den göra beräkringarna och returna värdet jag vill ha
    return int(km)*0.621371192

          
def miles_to_km (miles):
    return int(miles)*1.609344

if milesellerkm == "km":
    print(distance, "km i miles är:",km_to_miles(distance)) #distance var inputen och funktionen tar den och gör matten som behövs 
else:
    print(distance, "miles i km är:",miles_to_km(distance))