def tree_traversal(tree, path=None):
    if path is None:
        path = []
    for (node, children) in tree.items():
        new_path = path + [node]
        if children:
            for p in tree_traversal(children, new_path):
                yield p
        else:
            yield new_path