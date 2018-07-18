from abstract_data_types.linked_list import LinkedList


class UnionFind:
    def __init__(self, vertices):
        # a list of linked lists; each linked list represents a disjoint set for each unique vertex
        self.sets = [LinkedList() for _ in range(len(vertices)+1)]
        for i, vertex in enumerate(vertices):
            self.sets[i+1].append(vertex)
        # indices: vertex numbers; values: set # the vertex belongs to
        self.set_pointer = [x for x in range(len(vertices)+1)]

    def set_id(self, v):
        # gives the set # of a vertex
        return self.set_pointer[v]

    def union_sets(self, u, v):
        """
        Moves every vertex from the smaller set to the larger set, modifying set_pointer to reflect new set_id
        :param u: first of 2 vertices in an edge
        :param v: second of 2 vertices in an edge
        :complexity: O(X), where X is the size of the smaller of the 2 sets; delete and prepend are O(1) in linked lists
        """
        # swap v with u if the size of v set is smaller
        if len(self.sets[v]) < len(self.sets[u]):
            u, v = v, u
        # the sets to be unioned are determined by the sets vertices u and v belong to
        u_set, v_set = self.sets[self.set_pointer[u]], self.sets[self.set_pointer[v]]
        while len(u_set) > 0:
            # take a vertex from the smaller set u and allocate it to the set of vertex v
            vertex = u_set[0]
            # the vertex is now in set v, so we update the set_pointer for it
            self.set_pointer[vertex] = self.set_pointer[v]
            # remove the vertex from the u_set and add it to v_set
            u_set.delete(0)
            v_set.prepend(vertex)
