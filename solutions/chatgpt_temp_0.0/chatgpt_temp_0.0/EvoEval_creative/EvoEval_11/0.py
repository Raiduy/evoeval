from typing import List

def fruity_messages(fruits: List[str], location: str) -> str:
    if len(fruits) == 1:
        return f'Oh, are those {fruits[0]} from {location}? Marvelous!'
    elif len(fruits) == 2:
        return f'Oh, are those {fruits[0]} and {fruits[1]} from {location}? Marvelous!'
    else:
        fruit_str = ', '.join(fruits[:-1]) + f', and {fruits[-1]}'
        return f'Oh, are those {fruit_str} from {location}? Marvelous!'