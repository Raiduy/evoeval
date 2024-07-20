def magical_cafe(menu, magic_spell):
    new_menu = {}
    for (dish, price) in menu.items():
        transformed_dish = ''
        for i in range(len(dish)):
            transformed_dish += magic_spell[i % len(magic_spell)]
        new_menu[transformed_dish] = price
    return new_menu