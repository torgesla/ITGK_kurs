priskatalog = {'melk': 20, 'ost': 50, 'brød': 30}
element = priskatalog.get('melk')
samme_element = priskatalog['melk']
priskatalog['ketchup'] = 40  # evt. bruk .update({'ketchup':40}) hvis du skal legge til flere samtidig
print('Pris på melk:', element, samme_element)

priskatalog['melk'] = 15  # Kan ikke bruke .get('melk') når vi skal assigne ny verdi
print('Ny pris på melk:', priskatalog['melk'])
print('Antall par i priskatalog:', len(priskatalog))  # => Gir oss antall par i dictionariet

print(priskatalog.keys())
print(priskatalog.values())

for produkt, pris in priskatalog.items():
    print(f'{produkt} koster {pris} kroner.')
