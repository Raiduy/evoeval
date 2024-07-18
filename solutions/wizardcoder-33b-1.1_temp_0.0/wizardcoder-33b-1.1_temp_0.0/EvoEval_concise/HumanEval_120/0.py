
def maximum(arr, k):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[0], reverse=True)
    top_k = []
    for i in range(k):
        top_k.extend([sorted_dict[i][0]] * sorted_dict[i][1])
    return top_k