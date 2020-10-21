# Kont 2019
def print_dict(dictionary):
    for key, values in dictionary.items():
        print(f'{key}: {values}')


def read_file(filename):  # Read lines of file, and add to list
    with open(filename, mode='r', encoding='utf-8') as fil:
        return fil.readlines()


def fix_ingredients(streng):  # Remove leading and trailing whitespaces, and add to list
    renset_streng = streng.strip()
    liste_ord = renset_streng.split(', ')
    return liste_ord


def make_dict(foodlist):  # Make dict from unformatted file lines
    food_dict = {}
    for linje in foodlist:
        # We know that food name is on right side of colon, and ingredients on left
        navn, ingredisenser = linje.strip('\n').split(':')
        food_dict[navn] = fix_ingredients(ingredisenser)
    return food_dict


def print_recipe(food_dict, matrett):  # print info about a dish
    ingredisenser = food_dict[matrett]
    antall = len(ingredisenser)
    streng_del_2 = ', '.join(ingredisenser)
    print(f'{matrett} has {antall} ingredients: {streng_del_2}')


def all_recipies_with(food_dict):  # Create inverse dict ingredient - dish
    recipe_dishes = {}
    for dish, ingredients in food_dict.items():
        for ingredient in ingredients:  # Add dish to every ingredient key
            recipe_dishes[ingredient] = recipe_dishes.get(ingredient, [])  # Return empty list if new entry
            recipe_dishes[ingredient].append(dish)
    return recipe_dishes


def print_random_with_egg(food_dict):  # Print a random fish that contains egg
    import random
    recipe_dishes = all_recipies_with(food_dict)
    egg_dishes = recipe_dishes['egg']  # Retrieves the list og dishes containing egg
    random_dish = random.choice(egg_dishes)  # Picks a random element from egg_dishes
    print(f'Today you will be eating {random_dish}')
    print_recipe(food_dict, random_dish)


# Oppg 3-1 #
# food_liste = read_file('food.txt')
# print(food_liste)

# Oppg 3-2 #
# print(fix_ingredients('pannekaker: egg, mel, salt, melk\n'))

# Oppg 3-3 #
# food_dict = make_dict(food_liste)
# print(food_dict)

# Oppg 3-4 #
# print_recipe(food_dict, 'pannekaker')

# Oppg 3-5 #
# recipe_dishes = all_recipies_with(food_dict)
# print_dict(recipe_dishes)

# Oppgave 3-6 #
# print_random_with_egg(food_dict)
