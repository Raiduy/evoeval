def food_order(menu, order):
    if not order:
        return menu
    final_order = {}
    for (food_item, customization) in order.items():
        ingredients = list(menu[food_item])
        if 'remove' in customization:
            for ingredient in customization['remove']:
                ingredients.remove(ingredient)
        if 'add' in customization:
            for ingredient in customization['add']:
                ingredients.append(ingredient)
        final_order[food_item] = ingredients
    return final_order