def food_order(menu, order):
    if not order:
        return menu
    for food in order:
        if 'remove' in order[food]:
            for ingredient in order[food]['remove']:
                if ingredient in menu[food]:
                    menu[food].remove(ingredient)
        if 'add' in order[food]:
            for ingredient in order[food]['add']:
                if ingredient not in menu[food]:
                    menu[food].append(ingredient)
    return menu