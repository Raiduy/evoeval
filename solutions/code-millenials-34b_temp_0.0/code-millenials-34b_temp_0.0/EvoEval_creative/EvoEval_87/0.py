def word_spiral(arr):

    def spiral(arr):
        res = []
        while arr:
            res += arr.pop(0)
            arr = list(zip(*arr))[::-1]
        return res
    return ''.join(spiral(arr))