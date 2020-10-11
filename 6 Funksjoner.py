def printeFunksjon():
    print('Hei')

def printeFunksjon2(tekst_streng):
    print(tekst_streng)

def printeFunksjon3(navn):
    printeFunksjon2('Hei ' + navn)

def f(x): #Returnerer funksjonsverdien til uttrykket x^2 + 1 for en gitt x-verdi
    resultat = x**2 + 1
    return resultat

def navneLager(fornavn, etternavn):
    fullt_navn = fornavn + ' ' + etternavn
    return fullt_navn

def skrivUtListe(liste):
    for element in liste:
        print(element, end = '=>')

   