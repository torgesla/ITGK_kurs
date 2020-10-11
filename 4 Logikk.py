# Baserer seg på boolsk algebra

# & er OG/AND da må begge uttrykkene være sanne
True and True     # => True
True and False    # => False

# | er ELLER / OR, da må minst ett av uttrykkene være sanne
True or True     # => True
True or False    # => True
False or False   # => False 


if(bolsk_uttrykk):
    #Denne koden kjøres om uttrykket er True
elif(uttrykk2):
    #Hvis if failer, men uttrykk2 er sant
else:
    #Hvis begge failer er det denne som kjører

# Man MÅ ikke ha else hvis man har en if 
