
def Strongest_Extension(class_name, extensions):
    strongest_ext = extensions[0]
    strongest_diff = sum((1 for c in strongest_ext if c.isupper())) - sum((1 for c in strongest_ext if c.islower()))
    for ext in extensions[1:]:
        diff = sum((1 for c in ext if c.isupper())) - sum((1 for c in ext if c.islower()))
        if diff > strongest_diff:
            strongest_ext = ext
            strongest_diff = diff
    return f'{class_name}.{strongest_ext}'