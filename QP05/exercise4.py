def multi(g):
    edge_multiplicities = {}

    for pair in g:
        if pair in edge_multiplicities:
            edge_multiplicities[pair] += 1
        else:
            edge_multiplicities[pair] = 1

    triples_with_multiplicities = [(edge[0],multiplicity, edge[1]) for edge, multiplicity in edge_multiplicities.items()]

    return tuple(triples_with_multiplicities)


