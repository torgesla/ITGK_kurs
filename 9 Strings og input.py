""" navn = input('Skriv navnet ditt')
tall1 = int(input('Skriv et tall'))
tall2 = int(input('skriv et annet tall'))
print(f'Du heter {navn}, og summen av {tall1} og {tall2} er {tall1+tall2}')
 """
long_string = "I'll catch you if you fall - The floor"
print(long_string[:4])  # => I'll
print(long_string[-5:])  # => Floor
print(long_string[:-12])  # => I'll catch you if you fall
print(long_string[15:17].capitalize(), long_string[11:14], long_string[22:26], long_string[:4], long_string[5:10], long_string[18:21]+'.')

long_string_liste = long_string.split(' ')  # => Deler opp strengen ved mellomrom og legger ordene i en liste
print(long_string_liste[5])
