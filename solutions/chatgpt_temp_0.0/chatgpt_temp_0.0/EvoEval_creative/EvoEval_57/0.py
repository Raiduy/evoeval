def magical_cafe(menu, magic_spell):
    new_menu = {}
    spell_length = len(magic_spell)
    for (dish, price) in menu.items():
        transformed_dish = ''
        dish_length = len(dish)
        for i in range(dish_length):
            transformed_dish += magic_spell[i % spell_length]
        new_menu[transformed_dish] = price
    return new_menu