
def tri(n):
    if n == 0:
        return [3]
    elif n == 1:
        return [3, 1]
    elif n == 2:
        return [3, 1, 2]
    else:
        trib = [3, 1, 2]
        for i in range(3, n+1):
            if i % 2 == 0:
                trib.append(1 + i // 2)
            else:
                trib.append(trib[i-3] + trib[i-2] + trib[i-1])
        return trib
