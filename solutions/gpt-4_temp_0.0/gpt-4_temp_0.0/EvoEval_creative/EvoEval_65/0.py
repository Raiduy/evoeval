def food_order(menu, order):
    if not order:
        return menu
    final_order = menu.copy()
    for (food, changes) in order.items():
        if 'remove' in changes:
            for ingredient in changes['remove']:
                final_order[food].remove(ingredient)
        if 'add' in changes:
            final_order[food].extend(changes['add'])
    return final_order