def search_tree(key, tree):
    """given a string as key and the first node as tree, returns a pair (value, visited) or None if the key does not occur in the tree; the value is in the same tuple as key and visited is the list of keys that were visited in the search."""
    if tree is None:
        return None
    if key == tree[0]:
        return (tree[1], [key])
    if key < tree[0]:
        result = search_tree(key, tree[2])
        if result is None:
            return None
        return (result[0], [tree[0]] + result[1])
    else:
        result = search_tree(key, tree[3])
        if result is None:
            return None
        return (result[0], [tree[0]] + result[1])



    
