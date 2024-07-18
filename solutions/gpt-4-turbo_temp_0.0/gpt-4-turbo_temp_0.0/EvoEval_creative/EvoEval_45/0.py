def find_castle(arr):

    def view_count_from_hill(index):
        left_count = 0
        max_left_height = 0
        for i in range(index - 1, -1, -1):
            if arr[i] > max_left_height:
                left_count += 1
                max_left_height = arr[i]
            if arr[i] > arr[index]:
                break
        right_count = 0
        max_right_height = 0
        for i in range(index + 1, len(arr)):
            if arr[i] > max_right_height:
                right_count += 1
                max_right_height = arr[i]
            if arr[i] > arr[index]:
                break
        return left_count + right_count
    max_view = 0
    for i in range(len(arr)):
        max_view = max(max_view, view_count_from_hill(i))
    return max_view