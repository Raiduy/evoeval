def magical_cafe(menu, magic_spell):
    new_menu = {}
    spell_length = len(magic_spell)
    for (i, (dish, price)) in enumerate(menu.items()):
        new_dish = ''
        for (j, char) in enumerate(dish):
            new_dish += magic_spell[j % spell_length]
        new_menu[new_dish] = price
    return new_menu