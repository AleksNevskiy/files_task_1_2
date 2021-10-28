from pprint import pprint
import os

# path = os.path.join(os.getcwd(), 'recipes.txt')


def recipe_processor(path):
    with open(path, encoding='cp1251') as file:
        result = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for ingridients in range(counter):
                ingredient_name, quantity, measure = file.readline().split('|')
                temp_data.append(
                    {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
                )
            result[dish_name] = temp_data
            file.readline()
        return result

# with open(path, encoding='cp1251') as file:
cook_book = recipe_processor(os.path.join(os.getcwd(), 'recipes.txt'))
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        for j in cook_book[i]:
            if j['ingredient_name'] in res.keys():
                res[j['ingredient_name']]['quantity'] += int(j['quantity'])*person_count
            else:
                res[j['ingredient_name']] = {}
                res[j['ingredient_name']]['measure'] = j['measure']
                res[j['ingredient_name']]['quantity'] = int(j['quantity'])*person_count
    return res

pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))




