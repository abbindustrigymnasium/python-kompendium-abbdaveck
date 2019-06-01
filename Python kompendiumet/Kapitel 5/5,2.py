print("Hej vad heter du?")
namn = input()
print("Hur gammal är du?")
ålder = int(input())

if ålder>1: #om åldern är större än 1 kollar den nästa if-sats, om inte så är du 1 år gammal
    if ålder>2:
        if ålder>3:
            if ålder>4:
                if ålder>6:
                    if ålder>7:
                        if ålder>10:
                            if ålder>11:
                                if ålder>15:
                                    if ålder>16:
                                        print("Hej", namn,"du behöver 8 timmar sömn")
                                    else:
                                        print("Hej", namn, "du behöver 8,5 timmar sömn")
                                else:
                                    print("Hej", namn, "du behöver 9 timmar sömn")
                            else:
                                print("Hej", namn, "du behöver 9,5 timmar sömn")
                        else: 
                            print("Hej", namn, "du behöver 10 timmar sömn")
                    else: 
                        print("Hej", namn, "du behöver 10,5 timmar sömn")
                else: 
                    print("Hej", namn, "du behöver 11 timmar sömn")
            else: 
                print("Hej", namn, "du behöver 11,5 timmar sömn") 
        else: 
            print("Hej", namn, "du behöver 12 timmar sömn") 
    else: 
        print("Hej", namn, "du behöver 13 timmar sömn")    
else: 
    print("Hej", namn, "du behöver 14 timmar sömn")