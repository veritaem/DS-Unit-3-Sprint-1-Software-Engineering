import random
import itertools
from acme import *

list1=['Awesome','Shiny','Portable', 'Improved', 'Impressive']
list2=['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

names_list =list(itertools.product(list1, list2))
pick_1 = random.randint(len(names_list)
rando_int = random.randint(5, 101)
rando_fire = random.randint(0.0, 2.6)

def generate products(Class = Product, count = 30):
    prod_list = []
    prod_name_list = []
    prod_weight_list = []
    prod_flam_list = []
    prod_price_list = []
    # todo: figure out how to generate this?? all i need is the right method, i just dont know it in time..
    = Class(self.name)
    for count in count:
        prod_list.append()
        prod_name_list.append()
        prod_weight_list.append()
        prod_price_list.append()
        prod_flam_list.append()
        return prod_list

    

def inventory_report():
    print('number of unique products:', set(prod_name_list))
    print('Avg price', sum(prod_price_list) / len(prod_price_list)
    print('Avg weight', sum(prod_weight_list) / len(prod_weight_list))
    print('Avg flammability', sum(prod_flam_list) / len(prod_flam_list))


if __name__ == '__main__':
    inventory_report(generate_products())
