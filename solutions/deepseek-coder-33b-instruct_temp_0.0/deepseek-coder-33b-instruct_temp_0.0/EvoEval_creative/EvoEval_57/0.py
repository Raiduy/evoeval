def magical_cafe(menu, magic_spell):
    new_menu = {}
    spell_length = len(magic_spell)
    for (dish, price) in menu.items():
        new_dish = ''
        for i in range(len(dish)):
            new_dish += magic_spell[i % spell_length]
        new_menu[new_dish] = price
    return new_menu