def vampires_in_matrix(m: list):
    num_vampires = 0
    num_humans = 0
    for row in m:
        for cell in row:
            if cell == 2:
                num_vampires += 1
            elif cell == 1:
                num_humans += 1
    if num_vampires == 0:
        return 0
    else:
        return num_humans