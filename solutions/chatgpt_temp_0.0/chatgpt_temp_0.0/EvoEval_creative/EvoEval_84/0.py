def tree_traversal(tree):
    paths = []
    stack = [(tree, [])]
    while stack:
        (node, path) = stack.pop()
        if not node:
            continue
        path.append(list(node.keys())[0])
        if not node[list(node.keys())[0]]:
            paths.append(path)
        else:
            stack.append((node[list(node.keys())[0]], path.copy()))
            stack.append((node[list(node.keys())[1]], path.copy()))
    return paths