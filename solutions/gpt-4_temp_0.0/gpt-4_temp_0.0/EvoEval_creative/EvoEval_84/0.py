def tree_traversal(tree, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []
    for (node, children) in tree.items():
        new_path = path + [node]
        if children:
            tree_traversal(children, new_path, paths)
        else:
            paths.append(new_path)
    return paths