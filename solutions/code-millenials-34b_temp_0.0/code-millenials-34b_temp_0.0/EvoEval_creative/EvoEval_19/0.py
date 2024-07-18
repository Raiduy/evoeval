def vampires_in_matrix(m: list):
    humans_in_danger = 0
    vampire_rows = [0] * len(m)
    vampire_cols = [0] * len(m[0])
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                if vampire_rows[i] == 1 or vampire_cols[j] == 1:
                    humans_in_danger += 1
            elif m[i][j] == 2:
                vampire_rows[i] = 1
                vampire_cols[j] = 1
    return humans_in_danger