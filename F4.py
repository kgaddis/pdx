# Kainoa Gaddis (c) 2014
# F4
# Given nuber and set of edges, this code returns the depth of the tree


"""
write recursively rather than iteratively

first element is number of verticies

second element is the edges from one vertex to another

should return a number that shows the depth of the tree
 have a current node
 start where node is 0

start by finding the element with n-1 vertex number
"""

# e = (5, {(0, 1), (0, 2), (2, 3), (2, 4)})
# print(e[1])




def tree_depth(node, depth):

    for child in node:
        depth = max(tree_depth(node, depth+1))
    return depth
