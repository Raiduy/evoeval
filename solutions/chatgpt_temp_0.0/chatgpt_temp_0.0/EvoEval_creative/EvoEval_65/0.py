def food_order(menu, order):
    if not order:
        return menu
    for (food, customization) in order.items():
        if 'remove' in customization:
            for ingredient in customization['remove']:
                menu[food].remove(ingredient)
        if 'add' in customization:
            for ingredient in customization['add']:
                menu[food].append(ingredient)
    return menu