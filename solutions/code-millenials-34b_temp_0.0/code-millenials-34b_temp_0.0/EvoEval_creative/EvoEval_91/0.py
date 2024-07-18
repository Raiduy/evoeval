def spaceship_trajectory(spaceship_data):
    status = 'On Ground'
    for (action, distance) in spaceship_data:
        if action == 'Launch':
            if status == 'On Ground':
                status = 'In Space'
            else:
                return 'Invalid Action Sequence'
        elif action == 'Move':
            if status == 'In Space':
                pass
            else:
                return 'Invalid Action Sequence'
        elif action == 'Land':
            if status == 'In Space':
                status = 'On Ground'
            else:
                return 'Invalid Action Sequence'
    return status