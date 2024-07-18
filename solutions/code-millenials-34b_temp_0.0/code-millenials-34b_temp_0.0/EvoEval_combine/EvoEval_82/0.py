
def odd_fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        odd_fibfib_list = [0, 0, 1]
        for i in range(3, n + 1):
            temp = odd_fibfib_list[-1] + odd_fibfib_list[-2] + odd_fibfib_list[-3]
            if temp % 2 == 0:
                temp = int(''.join(str(temp)[::-1].split('0')[::-1]))
                if temp % 2 == 0:
                    temp = 0
            odd_fibfib_list.append(temp)
        return odd_fibfib_list[-1]