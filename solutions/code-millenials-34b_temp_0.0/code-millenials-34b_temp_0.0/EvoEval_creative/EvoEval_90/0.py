def magical_multiply(s1, s2):
    num1 = int(s1)
    num2 = int(s2)
    combinations = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            combinations.append(int(s1[i]) * int(s2[j]))
    return sum(combinations)