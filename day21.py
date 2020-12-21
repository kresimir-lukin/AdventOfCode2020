import sys

def build_ingredient_allergent_mapping(foods):
    potential_ingredient = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in potential_ingredient:
                potential_ingredient[allergen] = set(ingredients)
            else:
                potential_ingredient[allergen] &= set(ingredients)
    ingredient_allergent = {}
    while len(ingredient_allergent) < len(potential_ingredient):
        matched = [allergen for allergen, ingredients in potential_ingredient.items() if len(ingredients) == 1]
        for allergen in matched:
            ingredient = potential_ingredient[allergen].pop()
            ingredient_allergent[ingredient] = allergen
            for ingredients in potential_ingredient.values():
                if ingredient in ingredients:
                    ingredients.remove(ingredient)
    return ingredient_allergent

def part1(ingredient_allergent):
    not_in_allergens = 0
    for ingredients, _ in foods:
        not_in_allergens += sum(ingredient not in ingredient_allergent for ingredient in ingredients)
    return not_in_allergens

def part2(ingredient_allergent):
    sorted_by_allergen = sorted((allergen, ingredient) for ingredient, allergen in ingredient_allergent.items())
    return ','.join(map(lambda x: x[1], sorted_by_allergen))

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()

foods = []
for line in lines:
    bracket_index = line.index('(')
    ingredients, allergens = line[:bracket_index].split(), line[bracket_index + len('(contains '):-1].split(', ')
    foods.append((ingredients, allergens))

ingredient_allergent = build_ingredient_allergent_mapping(foods)

print(f'Part 1: {part1(ingredient_allergent)}, Part 2: {part2(ingredient_allergent)}')