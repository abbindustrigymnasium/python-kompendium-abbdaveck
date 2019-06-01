def echo(texten):
    print("|",texten)

def prompt(texten):
    return input(texten)

def line(bol=False):
    if bol == True:
        print("**********")
    else:
        print("----------")

def header(titel):
    längd = len(titel)
    meddelande = ""
    mitti = 10/längd 

    for i in range(1,int(mitti)*2+1):
        if i == 1:
                meddelande += "|" #1 är första värdet då sätter jag ut en |

        if i == int(mitti)*2+1: #avståndet till mitten gånger 2 plus 1 för att vi börjad på 1 får vi sista värdet
            meddelande += "|"
        meddelande += " "

        if i == int(mitti):
            meddelande += titel #vid mitten (mitti) lägger jag den faktiska texten
    print (meddelande)
