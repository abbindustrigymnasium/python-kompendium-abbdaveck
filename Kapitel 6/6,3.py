import requests

print("Artists Database:")
artists = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/").json()["artists"]
#hämtar en lista artiser och data gällande dem från en api
for i in artists:   #skriver ut varje namn som finns i listan
    print(i["name"])

print("")
print("Select artist:")
name = str(input())
print("")

names = ["Ariana Grande", "Avicii", "Blink-182", "Brad Paisley", "Ed Sheeran", "Imagine Dragons", "Maroon 5", "Scorpions"]

if name.title() in names:   #om inputen matchar någon namn i listan ovanför:
    for i in artists:   
        if i["name"] == name.title(): #välj endast raden i listan där inputen matchar namnet, dvs skriv bara ut den relevanta infon
            artistid = i["id"]
            infoartist = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + str(artistid)).json()
            print(infoartist["artist"]["name"])
            print("*************")
            print("Genres: ")
            for i in infoartist["artist"]["genres"]:
                print(i)
            print("Years active: " + infoartist["artist"]["years_active"][0])
            print("Members: ")
            for i in infoartist["artist"]["members"]:
                print(i)
            print("-------------")
else:
    print("Invalid input")   
