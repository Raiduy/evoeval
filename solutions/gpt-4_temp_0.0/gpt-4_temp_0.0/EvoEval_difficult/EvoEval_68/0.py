def pluck_and_replace(arr, replacement):
    if replacement in arr:
        return [-1, -1, replacement, -1]
    evens = [(val, idx) for (idx, val) in enumerate(arr) if val % 2 == 0 and val != replacement]
    if not evens:
        return []
    smallest = min(evens)
    arr[smallest[1]] = replacement
    return [smallest[0], smallest[1], replacement, arr.index(replacement)]