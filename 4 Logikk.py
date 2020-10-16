# Baserer seg på boolsk algebra

# and - begge uttrykkene må være sanne
True and True     # => True
True and False    # => False

# or - hvis minst ett av uttrykkene er sanne
True or True     # => True
True or False    # => True
False or False   # => False
# Comparison operators
var < 5
var > 5
var >= 5
var <= 5
var < 'abc'  # Funker for flere andre datastrukturer også, men tall er mest logisk. Her: alfabetisk rekkefølge

not True  # => False
not False  # => True
if(variable == 'hest')
if(variable != 'fisk')


if(bolsk_uttrykk):
    # Denne koden kjøres om uttrykket er True
elif(uttrykk2):
    # Hvis if failer, men uttrykk2 er sant
else:
    # Hvis begge failer er det denne som kjører

    # Man MÅ ikke ha else hvis man har en if


name = 'Torgeir'  # Forandre disse for annen oppførsel
age = 24

if(name == 'Torgeir' and age >= 16):
    print('Du kan holde kræsjkurs i ITGK')
elif(name == Torgeir or age >= 16):  # elif hoppes over hvis if-en kjører
    print('Du har enten feil alder eller feil navn')
