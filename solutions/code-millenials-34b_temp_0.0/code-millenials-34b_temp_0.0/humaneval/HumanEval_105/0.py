
def by_length(arr):
    num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    
    # Filter valid numbers
    valid_nums = [n for n in arr if 1 <= n <= 9]
    
    # Sort and reverse 
    sorted_nums = sorted(valid_nums, reverse=True)
    
    # Convert to words
    words = [num2words[n] for n in sorted_nums]
    
    return words
