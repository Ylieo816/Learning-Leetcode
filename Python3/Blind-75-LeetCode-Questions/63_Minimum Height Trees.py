# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

# leave node removal:  O(n)
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        node_num = n
        # check one node first
        if node_num == 1:
            return [0]
        
        # node adjanct:
        node_dict = defaultdict(set)
        for src, dst in edges:
            node_dict[src].add(dst)
            node_dict[dst].add(src)

        # find leaf node (only one connection)
        leave_node = []
        for node in node_dict:
            if len(node_dict[node]) == 1:
                leave_node.append(node)

        while node_num > 2:
            node_num -= len(leave_node)
            next_leave_node = []
            for leaf in leave_node:
                neighbor = node_dict[leaf].pop()
                node_dict[neighbor].remove(leaf)

                if len(node_dict[neighbor]) == 1:
                    next_leave_node.append(neighbor)
            leave_node = next_leave_node

        # final leave nodes are root node of minimum height trees
        return leave_node