
from typing import List

def parse_music_simplify(x: str, music_string: str) -> List[bool]:
    """ 
    Input to this function is a string, x, which is a fraction in the format of <numerator>/<denominator> where both numerator 
    and denominator are positive whole numbers and a string, music_string, representing musical notes in a special ASCII format.
    
    Your task is to parse the music_string and return a list of booleans corresponding to whether the beats of each note simplifies 
    the fraction x. 

    If x * beats evaluates to a whole number, add True to the list, otherwise add False. 

    Here is the legend for music_string:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    Example:
    parse_music_simplify("1/4", 'o o| .| o| o| .| .| .| .| o o')
    [True, False, False, False, False, False, False, False, False, True, True]
    """
    note_to_beats = {'o': 4, 'o|': 2, '.|': 1}
    (numerator, denominator) = map(int, x.split('/'))
    notes = music_string.split()
    results = []
    for note in notes:
        product = numerator * note_to_beats[note] / denominator
        if product.is_integer():
            results.append(True)
        else:
            results.append(False)
    return results