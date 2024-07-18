from typing import List

def fruity_messages(fruits: List[str], location: str) -> str:
    """
    Given a list of fruits and a location, return a string message in the following format:

    "Oh, are those <fruit> from <location>? Marvelous!"

    If you have two fruits, the message should say:

    "Oh, are those <fruit1> and <fruit2> from <location>? Marvelous!"

    If you have more than two fruit, the message should say:

    "Oh, are those <fruit1>, <fruit2> and <fruit3> from <location>? Marvelous!"

    The list of fruits will always contain at least one fruit.

    >>> fruity_messages(['apples','bananas'],'Florida')
    'Oh, are those apples and bananas from Florida? Marvelous!'

    >>> fruity_messages(['cherries'],'Michigan')
    'Oh, are those cherries from Michigan? Marvelous!'
    """
    if len(fruits) == 1:
        return f'Oh, are those {fruits[0]} from {location}? Marvelous!'
    elif len(fruits) == 2:
        return f'Oh, are those {fruits[0]} and {fruits[1]} from {location}? Marvelous!'
    else:
        fruits_list = ', '.join(fruits[:-1]) + f' and {fruits[-1]}'
        return f'Oh, are those {fruits_list} from {location}? Marvelous!'