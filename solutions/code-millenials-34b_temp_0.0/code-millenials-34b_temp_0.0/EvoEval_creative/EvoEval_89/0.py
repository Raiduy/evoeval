def space_invaders(aliens, ray):
    remaining_aliens = []
    for alien in aliens:
        if alien < ray - 1 or alien > ray + 1:
            remaining_aliens.append(alien)
    return remaining_aliens