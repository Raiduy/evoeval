
def by_length(arr):
    # Define a dictionary to map numbers to their names
    num_to_name = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 
                   6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    # Filter the array to only include numbers between 1 and 9
    arr = [num for num in arr if 1 <= num <= 9]
    
    # Sort the array in ascending order
    arr.sort()
    
    # Reverse the array
    arr.reverse()
    
    # Replace each number with its name
    arr = [num_to_name[num] for num in arr]
    
    return arr