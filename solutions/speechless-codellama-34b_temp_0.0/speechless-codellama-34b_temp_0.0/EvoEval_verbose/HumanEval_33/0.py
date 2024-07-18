

def sort_third(l: list):
    sorted_elements = []
    for i in range(len(l)):
        if i % 3 == 0:
            sorted_elements.append(l[i])
    sorted_elements.sort()
    l_prime = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_prime.append(sorted_elements.pop(0))
        else:
            l_prime.append(l[i])
    return l_prime