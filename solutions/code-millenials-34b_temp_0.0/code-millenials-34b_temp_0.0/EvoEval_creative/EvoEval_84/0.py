def tree_traversal(tree):

    def dfs(tree, path, paths):
        if not tree:
            paths.append(path)
            return
        for (k, v) in tree.items():
            dfs(v, path + [k], paths)
    paths = []
    dfs(tree, [], paths)
    return paths