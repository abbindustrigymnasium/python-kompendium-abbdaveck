import math

print("Skriv in ett flyttal")
flyttal = float(input())    #float gör så att det är ett tal men har med decimalerna
avrundat = math.ceil(flyttal)   #avrundar talet som skrev in
print(avrundat)
