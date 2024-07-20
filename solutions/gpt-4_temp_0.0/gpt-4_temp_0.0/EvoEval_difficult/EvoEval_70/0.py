def strange_sort_list(lst, lst2):
    merged = list(set(lst + lst2))
    odd_lst1 = sorted([i for i in merged if i in lst and i % 2 != 0])
    even_lst2 = sorted([i for i in merged if i in lst2 and i % 2 == 0])
    remaining = sorted([i for i in merged if i not in odd_lst1 and i not in even_lst2])

    def strange_sort(lst):
        result = []
        while lst:
            result.append(lst.pop(0))
            if lst:
                result.append(lst.pop())
        return result
    return strange_sort(odd_lst1 + even_lst2 + remaining)