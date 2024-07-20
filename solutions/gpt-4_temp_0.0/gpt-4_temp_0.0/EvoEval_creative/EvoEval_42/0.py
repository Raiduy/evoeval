def find_legendary_item(player_input):
    """
    In a popular multiplayer online game, players can acquire various items. Each item has a rarity value 
    ranging from 1 (common) to 5 (legendary). In a single game, a player can acquire multiple items but with 
    the condition that the rarity of each item is unique. The player_input is a list representing the items 
    acquired by a player in a single game, where each item is represented by its rarity.
    
    Your task is to write a function that determines if the player has acquired a legendary item (rarity 5) 
    in the game. The function should return True if a legendary item has been acquired and False otherwise. 

    Further, if a legendary item has been acquired, the function should return the rarity of the second most 
    valuable item that the player has acquired. If the player has only acquired the legendary item, return -1.

    The function should be able to handle player_input lists of any length.

    Examples:
        find_legendary_item([1, 2, 3, 4, 5]) == (True, 4)
        find_legendary_item([5]) == (True, -1)
        find_legendary_item([1, 3, 4]) == (False, None)
        find_legendary_item([]) == (False, None)
    """
    if 5 in player_input:
        player_input.remove(5)
        if len(player_input) == 0:
            return (True, -1)
        else:
            return (True, max(player_input))
    else:
        return (False, None)