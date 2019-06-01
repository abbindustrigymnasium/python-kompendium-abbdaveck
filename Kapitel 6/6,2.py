import requests

print("Skriv in namn på stad")
city = str(input()) #gör inputen till en string

cities = [  #städer i sringern
    "stockholm", 
    "uppsala",
]

if city.lower() in cities:
    forecasts = requests.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/' + city.lower()).json()["forecasts"]   
    #gör en request för värden från apien och tar de värden från city.lower och gör en lista
    print(forecasts[0]["date"] + " will be " + forecasts[0]["forecast"] )
    for i in forecasts:
        print(i["date"] + " will be " + i["forecast"])
else:
    print("Invalid city")