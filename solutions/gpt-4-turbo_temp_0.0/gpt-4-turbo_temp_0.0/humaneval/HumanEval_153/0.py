
def Strongest_Extension(class_name, extensions):
    # Initialize a variable to keep track of the strongest extension and its strength
    strongest_extension = None
    max_strength = float('-inf')  # Start with the lowest possible value

    # Iterate through each extension in the list
    for extension in extensions:
        # Calculate the strength of the extension
        CAP = sum(1 for char in extension if char.isupper())
        SM = sum(1 for char in extension if char.islower())
        strength = CAP - SM

        # Update the strongest extension if this extension is stronger
        if strength > max_strength:
            strongest_extension = extension
            max_strength = strength
        # If the strength is the same but this extension comes first, it remains unchanged

    # Return the class name combined with the strongest extension name
    return f'{class_name}.{strongest_extension}'
