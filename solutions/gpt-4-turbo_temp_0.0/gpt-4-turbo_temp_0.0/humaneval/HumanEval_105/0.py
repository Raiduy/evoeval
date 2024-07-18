
def by_length(arr):
    # Dictionary to map numbers to their names
    number_names = {
        1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    
    # Filter the array to include only numbers between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered array
    sorted_arr = sorted(filtered_arr)
    
    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]
    
    # Replace each number with its corresponding name
    result = [number_names[num] for num in reversed_arr]
    
    return result
