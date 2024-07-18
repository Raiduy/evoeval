from typing import List


def parse_music(music_string: str) -> List[int]:
    """ 
    This function takes as input a string that represents musical notes. These musical notes are represented 
    in a unique ASCII format. Each character or set of characters corresponds to a distinct musical note 
    with a specific duration, measured in beats. 

    The function's job is to parse the input string and translate it into a list of integers. Each integer 
    in the returned list corresponds to the number of beats for the respective musical note in the input string.

    The mapping from characters to beats is defined as follows:
    - 'o' is a whole note, which lasts for four beats
    - 'o|' is a half note, and it lasts for two beats
    - '.|' is a quarter note, and it only lasts for one beat

    So, the function should read each musical note from the input string, convert it to the corresponding 
    number of beats using the mapping, and return a list of these beat counts in the same order as the notes 
    appeared in the input string.

    For instance, if the function is called with the input string 'o o| .| o| o| .| .| .| .| o o', the function 
    should return the list [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]. This list indicates that the first note in the 
    string is a whole note lasting four beats, the second note is a half note lasting two beats, and so on.

    Args:
    music_string (str): A string representing musical notes in a special ASCII format.

    Returns:
    List[int]: A list of integers where each integer represents the number of beats a note lasts for.
    """
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    notes = music_string.split()
    beats = [beat_mapping[note] for note in notes]
    return beats