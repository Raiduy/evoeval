
def move_one_ball(arr):
    # Check if the array is empty or already sorted
    if not arr or arr == sorted(arr):
        return True
    
    # Find the index where arr[i] > arr[i+1]
    shift_point = -1
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if shift_point == -1:
                shift_point = i + 1
            else:
                # If we find more than one point where arr[i] > arr[i+1],
                # it means we cannot sort the array with right shifts
                return False
    
    # If no shift point was found, the array is already non-decreasing
    if shift_point == -1:
        return True
    
    # Perform the right shift operation
    shifted_arr = arr[shift_point:] + arr[:shift_point]
    
    # Check if the shifted array is sorted
    return shifted_arr == sorted(shifted_arr)
