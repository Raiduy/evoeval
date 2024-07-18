def tree_traversal(tree):

    def traverse(node, path, paths):
        if not node:
            return
        if not node.values():
            paths.append(path)
            return
        for (key, value) in node.items():
            traverse(value, path + [key], paths)
    paths = []
    for (root, children) in tree.items():
        traverse(children, [root], paths)
    return paths