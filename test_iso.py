import unittest
import simple
import optimized

# Some undirected graphs.
graph_1 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
graph_2 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['X']}  # isomorphic to graph_1
graph_3 = {'A': ['B', 'C'], 'B': ['A', 'C'],
           'C': ['A', 'B']}  # not isomorphic to g1
graph_4 = {'X': ['Y', 'Z'], 'Y': ['X'], 'Z': ['Y']}  # not isomorphic to g1
graph_5 = {'A': ['A', 'U'], 'C': ['A'], 'U': ['A']}  # isomorphic to g1
graph_6 = {'J': ['J', 'U'], 'C': ['J', 'C'], 'U': ['J']}  # iso to 7
graph_7 = {'A': ['A', 'U'], 'U': ['A'], 'C': ['C', 'A']}  # iso to 6
graph_8 = {'A': ['B', 'C'], 'C': ['A'], 'B': ['A']} # iso to 1, keys turned around
graph_9 = {'A': ['U', 'C'], 'C': ['A'], 'U': ['A']} # iso to 1 and 8, keys tunred around and B -> U
graph_10 = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A']}
graph_11 = {}

# There should be a better way to test each implementation with the same harness without copypasting this....

class TestIsomorphism(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(simple.is_isomorphic(graph_1, graph_2)) # Simple case (renames)
        self.assertTrue(simple.is_isomorphic(graph_2, graph_1)) # Inverse of the previous test

        self.assertTrue(simple.is_isomorphic(graph_1, graph_8)) # Switch around keys

        self.assertTrue(simple.is_isomorphic(graph_1, graph_8)) # Also rename B to U

        self.assertTrue(simple.is_isomorphic(graph_6, graph_7)) # random test

        self.assertFalse(simple.is_isomorphic(graph_1, graph_7)) # Obviously not isomorphic

        self.assertFalse(simple.is_isomorphic(graph_1, graph_10)) # Degree distribution does not match

        self.assertFalse(simple.is_isomorphic(graph_10, graph_11)) # Handle empty graphs


    def test_optimized(self):
        self.assertTrue(optimized.is_isomorphic(graph_1, graph_2)) # Simple case (renames)
        self.assertTrue(optimized.is_isomorphic(graph_2, graph_1)) # Inverse of the previous test

        self.assertTrue(optimized.is_isomorphic(graph_1, graph_8)) # Switch around keys

        self.assertTrue(optimized.is_isomorphic(graph_1, graph_8)) # Also rename B to U

        self.assertTrue(optimized.is_isomorphic(graph_6, graph_7)) # random test
        
        self.assertFalse(simple.is_isomorphic(graph_1, graph_10)) # Degree distribution does not match

        self.assertFalse(simple.is_isomorphic(graph_1, graph_11)) # Handle empty graphs

if __name__ == '__main__':
    unittest.main()