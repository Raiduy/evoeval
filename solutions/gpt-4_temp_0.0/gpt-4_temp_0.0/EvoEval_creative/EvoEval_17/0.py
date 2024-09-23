def wizard_battle(dragon_hp: int, wizards: list) -> str:
    """ Return the name of the wizard who defeated the dragon, given the dragon's hit points (HP) and
    an ordered list with the name of the wizard and their magic power:
        - The wizard's magic reduces the dragon's HP by their magic power. 
        - Wizards take turns in the order they are listed, and they only get to attack once.
        - The dragon is defeated when its HP is reduced to 0 or less.

    If none of the wizards can defeat the dragon return 'The dragon won!'

    Note that the wizards are a list of tuples, where each tuple has the wizard's name as a string and
    their magic power as an integer. The dragon's HP is a positive integer.

    >>> wizard_battle(20, [('Gandalf', 15), ('Merlin', 10), ('Dumbledore', 30)])
    'Merlin'
    >>> wizard_battle(100, [('Harry', 25), ('Ron', 20), ('Hermione', 30), ('Luna', 10)])
    'The dragon won!'
    >>> wizard_battle(65, [('Newt', 15), ('Tina', 20)])
    'The dragon won!'
    """
    for wizard in wizards:
        dragon_hp -= wizard[1]
        if dragon_hp <= 0:
            return wizard[0]
    return 'The dragon won!'