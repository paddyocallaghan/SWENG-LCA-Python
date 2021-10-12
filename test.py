import unittest
import lca

class TestLca(unittest.TestCase):

    def test_node0_1(self):
        self.assertEqual(lca.getLCA(lca.root, 0, 1).key, 0)

    def test_node1_2(self):
        self.assertEqual(lca.getLCA(lca.root, 1, 2).key, 0)

    def test_2_3(self):
        self.assertEqual(lca.getLCA(lca.root, 2, 3).key, 0)

    def test_node3_4(self):
        self.assertEqual(lca.getLCA(lca.root, 3, 4).key, 1)

    def test_4_5(self):
        self.assertEqual(lca.getLCA(lca.root, 4, 5).key, 0)

    def test_node5_6(self):
        self.assertEqual(lca.getLCA(lca.root, 5, 6).key, 2)

    def test_node_none(self):
        self.assertEqual(lca.getLCA(None, 0, 0), None)

    def test_node_false(self):
        self.assertEqual(lca.getLCA(lca.root, 100, 100), None)


if __name__ == '__main__':
    unittest.main()