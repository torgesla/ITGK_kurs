liste = [1, 2, 3, [2, 4, 5], 'hest']

første_element = liste[0]  # => 1
siste_element = liste[-1]  # => 'hest'
nest_siste_element = liste[-2]  # => [2, 4, 5]
nøstet_liste_element = liste[3][1]  # => 4

liste[1] = 'LUR'  # => [1, 'LUR', 3, [2, 4, 5], 'hest']

liste_sliced = liste[:4]  # => [1, 'LUR', 3, [2, 4, 5]]

################    Tuppler, immutable/ kan ikke forandres på etter init     ###################
tuppel = (1, 2, 3, 4, 5)
# tuppel[1] = '7' # => TypeError: 'tuple' object does not support item assignment
