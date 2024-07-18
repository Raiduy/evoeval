def wizard_battle(dragon_hp: int, wizards: list) -> str:
    """ Return the name of the wizard who defeated the dragon, given the dragon's hit points (HP) and
    an ordered list with the name of the wizard and their magic power:
        - The wizard's magic reduces the dragon's HP by their magic power. 
        - Wizards take turns in the order they are listed, and they only get to attack once.
        - The dragon is defeated when its HP is reduced to 0 or less.

    If none of the wizards can defeat the dragon return 'The dragon won!'

    Note that the wizards are a list of tuples, where each tuple has the wizard's name as a string and
    their magic power as an integer. The dragon's HP is a positive integer.
    """
    for wizard in wizards:
        (name, power) = wizard
        dragon_hp -= power
        if dragon_hp <= 0:
            return name
    return 'The dragon won!'