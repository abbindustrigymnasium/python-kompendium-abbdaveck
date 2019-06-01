print("Hej hur gammal är du?")
ålder = input()
myndig = 18 - int(ålder)    #int ser till att värdet är en siffra och inte ett ord om det är en siffra går det att utföra beräkningar med det
print("Du är myndig om", myndig, "år!")