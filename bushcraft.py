from time import sleep

# Variabelen
Personen = 5
positive = ["ja", "Ja", "JA", "j", "J", "jA", "yes", "YES"]
negative = ["nee", "Nee", "NEE", "n", "N", "nEE", "NeE", "nEe", "no", "NO"]
# Het totaal


# User Defined Functions

def showIntro():
    print('Welkom bij deze aanmeldprogramma voor bushcraft')
    sleep(1)
    print('Er zijn een aantal criteria waaraan je moet voldoen')

# Code start ---

showIntro()
sleep(1)
# Reiskosten
DieselPrijs = float(input('Mijn auto verbruikt 1 liter op 12 km en de afstand ernaartoe is 244 km. Hoeveel kost diesel per liter? '))
DieselTotaal = (244 / 12) * DieselPrijs
DieselTotaal += DieselTotaal
ZelfBetalen = 0.2 * DieselTotaal
print('De literprijs voor 244 km, heen en terug, is in totaal €'+ str(DieselTotaal) +' + €8 euro voor koffie en brood')
sleep(1.5)
BetalenZelf = input('Ben je bereid om zelf 1/5e deel van €'+ str(DieselTotaal) +', wat €'+ str(ZelfBetalen) +' is, met daarboven op €8 euro voor het eten te betalen? ')
if BetalenZelf in positive:
    sleep(1)
    # Materialen en voedsel
    Pemmican = float(input('Wat is de prijs van een pak pemmican-reepjes? '))
    Vijgen = float(input('Wat is de prijs van vijgenplakjes per stuk? '))
    Scheepsbiscuit = float(input('Wat is de prijs van scheepsbiscuit per rol? '))
    Firesteels = float(input('Wat is de prijs van firesteels per stuk? '))
    Lucifers = float(input('Wat is de prijs van lucifers per pak? '))
    Vuursteen = float(input('Wat is de prijs van een originele vuursteen? '))
    Sisaltouw = float(input('Wat is de prijs van een sisaltouw per 2 meter? '))
    # De prijzen van de materialen worden hier berekend voor 5 personen
    MaterialenPrijs = ((Pemmican * 2) * 5) + ((Vijgen * 3) * 5) + (Scheepsbiscuit * 2) + (Firesteels * 2) + (Lucifers * 5) + (Vuursteen * 4) + (Sisaltouw * 20)
    sleep(1)
    # Hier wordt gekeken of de kandidaat aan alle eisen voldoet
    print('Volgende stap! Ik ga kijken of je gepast bent om een mede-held te zijn!')
    sleep(1.3)
    Leeftijd = int(input('Hoe oud ben je? '))
    Flexibel = input('Ben jij flexibel? ')
    Doorzet = input('Ben jij doorzettend? ')
    if Leeftijd >= 16 and Flexibel in positive and Doorzet in positive:
        print('Goed, nu gaan we verder met een aantal paar vragen om jouw rol te bepalen...')
        sleep(1)
        print('Ik heb 4 rollen die vervuld moeten worden en de aan hand van deze vragen, kan ik bepalen welke rol het beste bij je past.')
        sleep(1)
        # Beer-vragen
        Bankdruk = int(input('Hoeveel kilogram kun je bankdrukken? '))
        Pushup = int(input('Hoevaak kun je opdrukken? '))
        Gewicht = int(input('Hoeveel kilogram kun je met een dumbbell heffen? '))
        Massa = int(input('Wat is jouw massa in kg? (Alleen massa erin zetten) '))
        # Uil vragen
        IQ = int(input('Wat is jouw IQ? '))
        Hoofdstad = input('Wat is hoofdstad van Albanië? ')
        


    else:
        print('Helaas ben jij niet gepast omdat je jong/niet flexibel/niet doorzettend bent!')
elif BetalenZelf in negative:
    print('Geld groeit niet van de bomen!')
else:
    print('Ik begrijp het niet bro')
    