def tree_traversal(tree):

    def dfs(node, path):
        if not tree[node]:
            paths.append(path + [node])
            return
        for child in tree[node]:
            dfs(child, path + [node])
    paths = []
    dfs(list(tree.keys())[0], [])
    return paths