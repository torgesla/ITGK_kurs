i = 0
while(True):  # Kjører evig eller til den breakes
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
