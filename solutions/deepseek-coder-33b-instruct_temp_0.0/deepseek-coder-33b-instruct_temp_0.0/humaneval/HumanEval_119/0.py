
def match_parens(lst):
    def is_balanced(s):
        balance = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    for perm in [''.join(p) for p in permutations(lst)]:
        if is_balanced(perm):
            return 'Yes'
    return 'No'
