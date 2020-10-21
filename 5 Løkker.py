# Vi bruker while hvis vi ikke vet på forhånd hvor mange iterasjoner som skal kjøre, ellers for.
i = 0
while(True):  # Kjører evig eller til den breakes.
    if (i >= 2):  # Bryt ut av løkken hvis i >= 2
        break
    print(i, ': While-true med break')
    i += 1

j = 0
while(j < 5):
    print(j, ': While med betingelse')
    j += 1

###########################################################################

for i in range(10):
    print(i)

for i in range(2, 5):
    print(i, ' range med start og stopp')

liste = ['hei', 'bamse', 'fisk']

for element in liste:  # for loop
    print(element)

for index in range(len(liste)):  # indeksering av listen
    print(index, ': ', liste[index])

for index, element in enumerate(liste):  # Bruk av enumerate
    print(index, ': ', element)

for bokstav in 'Rumba med Gunn':
    print(bokstav)

matrise = [['00', '01', '02'],
           ['10', '11', '12'],
           ['20', '21', '22'],
           ['30', '31', '32'],
           ['40', '41', '42']]

for radNr in range(len(matrise)):
    for kolonneNr in range(len(matrise[radNr])):
        print(f'Rad nr. {radNr} og kolonne nr. {kolonneNr} gir verdi {matrise[radNr][kolonneNr]}')

for rad in matrise:
    for celle in rad:
        print(celle)

# etter 46: rad = ['00', '01', '02'], celle is not defined
# etter 47: rad = ['00', '01', '02'], celle = '00'
# etter 47: rad = ['00', '01', '02'], celle = '01'
# etter 47: rad = ['00', '01', '02'], celle = '02'
# etter 46: rad = ['10', '11', '12'], celle = '02'
# etter 46: rad = ['10', '11', '12'], celle = '10'
