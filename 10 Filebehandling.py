import os
import sys

with open(os.path.join(sys.path[0], 'tekstfil.txt'), mode='r', encoding='utf-8') as tekstfil:
    tekstfil_innhold = tekstfil.read()
# print(tekstfil.readline())
print(tekstfil_innhold)
innhold_liste = tekstfil_innhold.split('\n')  # Splitter på linjeskift(\n)
print(repr(tekstfil_innhold))  # Skriver ut tekstfilen slik den lese av maskinen inkl. escape characters

with open('skrivefil.txt', mode='w', encoding='utf-8') as skrivefil:
    skrivefil.write('Nå skriver jeg til filen\nDette er en ny linje')

with open('skrivefil.txt', mode='r', encoding='utf-8') as lesefil:
    print(lesefil.read())
