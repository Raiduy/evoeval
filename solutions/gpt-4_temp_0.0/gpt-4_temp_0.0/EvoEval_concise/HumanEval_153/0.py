
def Strongest_Extension(class_name, extensions):
    """
    Given a class name (string) and a list of extensions, this function loads the strongest extension to the class. 
    The strength of an extension is defined as the difference between the count of uppercase letters (CAP) and the 
    count of lowercase letters (SM) in its name. In case of a tie, the first extension in the list wins. The function 
    returns a string in the format 'ClassName.StrongestExtensionName'.
    
    Example:
    Strongest_Extension('my_class', ['AA', 'Be', 'CC']) returns 'my_class.AA'
    """
    strongest_extension = ''
    strongest_strength = -1
    for extension in extensions:
        strength = sum((1 for char in extension if char.isupper())) - sum((1 for char in extension if char.islower()))
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength
    return f'{class_name}.{strongest_extension}'