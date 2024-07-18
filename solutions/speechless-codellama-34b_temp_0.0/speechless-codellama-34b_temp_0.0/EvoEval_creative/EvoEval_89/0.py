def space_invaders(aliens, ray):
    remaining_aliens = []
    for i in range(len(aliens)):
        if aliens[i] % 2 == 0 and aliens[i] != ray:
            remaining_aliens.append(aliens[i])
        elif aliens[i] == ray:
            remaining_aliens.remove(aliens[i])
            if i > 0 and aliens[i - 1] % 2 == 0:
                remaining_aliens.remove(aliens[i - 1])
            if i < len(aliens) - 1 and aliens[i + 1] % 2 == 0:
                remaining_aliens.remove(aliens[i + 1])
    return remaining_aliens