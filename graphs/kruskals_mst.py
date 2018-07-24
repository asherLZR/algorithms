from abstract_data_types.union_find import UnionFind

# initialisation of input values
vertex_count, edge_count = map(int, input().split())
U, V, W = [0] * edge_count, [0] * edge_count, [0] * edge_count
for i in range(edge_count):
    U[i], V[i], W[i] = map(int, input().split())
edge_list = sorted(zip(U, V, W), key=lambda x: x[2])

# union find data structure for each unique vertex in the edge list
union_find = UnionFind(list(set(x for x in U + V)))
finalised = []
mst_weight = 0

# continually try adding edges in sorted order provided they do not create a cycle
for u, v, w in edge_list:
    # if the 2 vertices are in disjoint sets, there is no cycle
    if union_find.set_id(u) != union_find.set_id(v):
        # add the edge to the finalised graph
        finalised.append((u, v, w))
        # union the sets of both vertices incident to the edge
        union_find.union_sets(u, v)
        mst_weight += w
    # break once the number of edges is that of a tree, |V|-1
    if len(finalised) == vertex_count - 1:
        break
print(mst_weight)

# 4 6
# 1 2 5
# 1 3 3
# 4 1 6
# 2 4 7
# 3 2 4
# 3 4 5