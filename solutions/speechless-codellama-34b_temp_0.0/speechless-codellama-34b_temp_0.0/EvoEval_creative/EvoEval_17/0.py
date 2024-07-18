def wizard_battle(dragon_hp: int, wizards: list) -> str:
    for wizard in wizards:
        dragon_hp -= wizard[1]
        if dragon_hp <= 0:
            return wizard[0]
    return 'The dragon won!'