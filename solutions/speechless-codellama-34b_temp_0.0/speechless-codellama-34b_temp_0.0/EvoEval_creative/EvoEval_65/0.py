def food_order(menu, order):
    if not order:
        return menu
    for (food, customization) in order.items():
        if food not in menu:
            continue
        ingredients = menu[food]
        if 'remove' in customization:
            ingredients = [ingredient for ingredient in ingredients if ingredient not in customization['remove']]
        if 'add' in customization:
            ingredients.extend(customization['add'])
        menu[food] = ingredients
    return menu