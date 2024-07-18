
def by_length(arr):
    # Define a dictionary to map numbers to their corresponding names
    num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # Filter out any strange numbers from the array
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the filtered array in descending order
    sorted_arr = sorted(filtered_arr, reverse=True)
    
    # Map each number in the sorted array to its corresponding name
    result = [num_to_name[num] for num in sorted_arr]
    
    return result
