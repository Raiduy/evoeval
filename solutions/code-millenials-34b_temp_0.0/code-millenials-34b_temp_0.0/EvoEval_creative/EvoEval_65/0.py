def food_order(menu, order):
    if not order:
        return menu
    final_order = menu.copy()
    for (food, customizations) in order.items():
        if food in final_order:
            if 'remove' in customizations:
                for ingredient in customizations['remove']:
                    if ingredient in final_order[food]:
                        final_order[food].remove(ingredient)
            if 'add' in customizations:
                final_order[food].extend(customizations['add'])
    return final_order