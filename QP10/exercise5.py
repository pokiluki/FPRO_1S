def transitive_closure(r):
    def aux(raux):
        resul =set([(x[0],y[1]) for x in raux for y in raux if x[1] == y[0]]) | raux
        if len(resul) == len(raux):
            return resul
        else:
            return aux(resul)
    return aux(r)

