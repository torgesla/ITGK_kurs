print('Hello world!')       # => Hello World
print('Hello', 'World')    # => Hello World
print('Husk' + 'Mellomrom')  # => HuskMellomrom

streng1 = 'Hello'
streng2 = 'World'
print(streng1, streng2)     # => Hello World

årstall = 2020
print(f'I år er {årstall}')  # => I år er det 2020
print('I fjor var det år', årstall - 1)    # => I fjor var det år 2019
# print('Neste år er det' + (årstall + 1))  # => TypeError: fordi vi kombinerer forskjellige typer

print('I ' + str(årstall) + ' må vi da bruke str()')  # => I 2020 må vi da bruke str()

print('Her leker jeg med ', end='')  # default er newline, her er det ingen end character
print('end-argumentet. Og her setter jeg end til å være:', end=' fisk')  # Alt kan være en end-argument. Komma, newline(\n), bindestrek, tab(\t)
