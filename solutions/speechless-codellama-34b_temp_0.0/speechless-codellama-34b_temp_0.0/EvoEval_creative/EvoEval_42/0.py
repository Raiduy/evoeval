def find_legendary_item(player_input):
    legendary_acquired = False
    second_most_valuable_rarity = -1
    for item in player_input:
        if item == 5:
            legendary_acquired = True
        elif item > second_most_valuable_rarity:
            second_most_valuable_rarity = item
    return (legendary_acquired, second_most_valuable_rarity)