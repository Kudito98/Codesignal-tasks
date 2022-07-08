def solution(adj):
    degseq = list(map(sum, adj))
    
    if sorted(degseq) in [[1, 1, 2, 2, 4], [1, 1, 2, 3, 3]]:
        # These degree sequences are unique up to isomorphism.
        return True
    
    elif sorted(degseq) == [1, 2, 2, 2, 3]:
        # There are two graphs on this degree sequence. In the graph
        # we want, all vertices of degree 2 are adjacent to the vertex
        # of degree 3.
        i = degseq.index(3)
        return all(row[i] for row in adj if sum(row) == 2)

    return False
