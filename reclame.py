from algemene_functies import mijn_functie_2
#aanbieding 1:
def aanbieding_1():
    smaak="aardbei"
    prijs=4
    korting = prijs*0.1
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - korting} euro.")
aanbieding_1()
#inkomsten :
def inkomsten_totaal():
    btw = 0.09
    totaal=220+430+125+160+205+90+345
    bedrag = float(totaal * btw)    
    print(f"Het totaal van inkomsten deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")
inkomsten_totaal()
#laag en hoog
def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return hoog, laag
print(laag_en_hoog([220,430,125,160,205,90,345]))
#gemiddelde
def gemiddelde(mijn_lijst):
    gemiddelde= sum(mijn_lijst)/7
    print(f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro")
gemiddelde([220,430,125,160,205,90,345])
#meervoudig
def meervoudig(invoer_lijst):
    resultaat= laag_en_hoog(invoer_lijst)
    return resultaat
print(meervoudig([10,5,3,2,1,2,9]))
#combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    getal1_hoog= korte_lijst[0]
    getal2_laag= korte_lijst[1]
    resultaat=mijn_functie_2(getal1_hoog, getal2_laag)
    return resultaat
print(combinatie([10,5,3,2,1,2,9]))