
def Strongest_Extension(class_name, extensions):

    def calculate_strength(extension):
        CAP = sum((1 for char in extension if char.isupper()))
        SM = sum((1 for char in extension if char.islower()))
        return CAP - SM
    strengths = [(calculate_strength(ext), ext) for ext in extensions]
    strongest_extension = sorted(strengths, key=lambda x: x[0], reverse=True)[0][1]
    return f'{class_name}.{strongest_extension}'