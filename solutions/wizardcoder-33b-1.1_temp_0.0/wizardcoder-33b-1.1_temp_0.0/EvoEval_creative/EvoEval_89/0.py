def space_invaders(aliens, ray):
    return [alien for alien in aliens if alien != ray and alien != ray - 1 and (alien != ray + 1)]