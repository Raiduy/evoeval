def wizard_battle(dragon_hp: int, wizards: list) -> str:
    for (wizard, magic_power) in wizards:
        dragon_hp -= magic_power
        if dragon_hp <= 0:
            return wizard
    return 'The dragon won!'