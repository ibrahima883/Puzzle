import unittest
import Projet
class Test_project(unittest.TestCase):
    '''
    Class of test to validate your developments.
    Please note that for some cases, multiple lists of edges are correct.
    '''
    def test_Case_1(self):

        edges = Projet.computeEdges("Projet_Cas_1.txt")
        expectedResults = [[0, 2], [8, 2]]

        self.assertEqual(2, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_2(self):

        edges = Projet.computeEdges("Projet_Cas_2.txt")
        print edges
        expectedResults = [[0, 2], [0, 2], [3, 2], [3, 2]]

        self.assertEqual(4, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_3(self):

        edges = Projet.computeEdges("Projet_Cas_3.txt")
        expectedResults = [[8, 7], [8, 2], [0, 2], [2, 8], [6, 7]]

        self.assertEqual(5, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_4(self):

        edges = Projet.computeEdges("Projet_Cas_4.txt")
        expectedResults = [[0, 1], [11, 9], [11, 9], [11, 3], [11, 3], [3, 1], [9, 1], [9, 1]]

        self.assertEqual(8, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_5(self):

        edges = Projet.computeEdges("Projet_Cas_5.txt")
        expectedResults = [[6, 16], [6, 16], [0, 2], [0, 2], [0, 15], [0, 15], [3, 4], [3, 4], [3, 2], [3, 2], [12, 17], [12, 17], [12, 2], [12, 14], [12, 14], [4, 14], [4, 14], [15, 16]]

        self.assertEqual(18, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_6(self):

        edges = Projet.computeEdges("Projet_Cas_6.txt")
        expectedResults = [[5, 3], [8, 11], [8, 15], [3, 0], [17, 15], [0, 21], [8, 11], [29, 34], [21, 25], [34, 13], [13, 11], [13, 11], [25, 11]]

        self.assertEqual(13, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_7(self):

        edges = Projet.computeEdges("Projet_Cas_7.txt")
        expectedResults = [[10, 14], [1, 0], [1, 0], [1, 3], [1, 5], [1, 5], [4, 5], [4, 5], [4, 12], [4, 12], [7, 15], [7, 15], [7, 5], [7, 5], [5, 13], [12, 13], [15, 14], [15, 14], [13, 14]]

        self.assertEqual(19, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_8(self):

        edges = Projet.computeEdges("Projet_Cas_8.txt")
        expectedResults = [[6, 4], [6, 4], [9, 41], [24, 0], [34, 18], [0, 2], [0, 2], [4, 20], [4, 20], [4, 2], [4, 2], [52, 44], [52, 44], [52, 51], [52, 60], [52, 60], [52, 55], [52, 55], [57, 60], [57, 60], [57, 49], [57, 49], [18, 20], [41, 44], [41, 44], [60, 61], [63, 55], [63, 55], [47, 45], [47, 23], [44, 20], [20, 23], [45, 47]]

        self.assertEqual(33, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_9(self):

        edges = Projet.computeEdges("Projet_Cas_9.txt")
        expectedResults = [[0, 1], [0, 2], [3, 2], [3, 1], [0, 1], [2, 3]]

        self.assertEqual(6, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_10(self):

        edges = Projet.computeEdges("Projet_Cas_10.txt")
        expectedResults = [[0, 2]]

        self.assertEqual(1, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_11(self):

        edges = Projet.computeEdges("Projet_Cas_11.txt")
        expectedResults = [[4, 3], [29, 28], [3, 2], [44, 43], [59, 58], [28, 27], [0, 1], [0, 5], [5, 10], [10, 15], [15, 20], [20, 25], [1, 26], [2, 27], [25, 40], [26, 41], [27, 42], [40, 45], [45, 50], [50, 55], [55, 60], [65, 66], [65, 60], [41, 42], [66, 67], [43, 58], [42, 57], [58, 63], [67, 68], [63, 68]]

        self.assertEqual(30, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_12(self):

        edges = Projet.computeEdges("Projet_Cas_12.txt")
        expectedResults = [[1, 2], [2, 7], [9, 14], [14, 13], [15, 16], [10, 11], [10, 11], [6, 11], [6, 7], [11, 12], [16, 17], [7, 8], [7, 12], [8, 13], [12, 13], [12, 17], [13, 18], [18, 17], [17, 22], [23, 22]]

        self.assertEqual(20, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            expectedResults[i].sort()

        edges.sort()
        expectedResults.sort()
        self.assertListEqual(edges, expectedResults)

    def test_Case_13(self):

        edges = Projet.computeEdges("Projet_Cas_13.txt")
        print edges

        results=[[22, 505], [22, 505], [22, 13], [22, 13], [34, 44], [34, 44], [34, 149], [34, 149], [34, 32], [34, 32], [143, 149], [143, 149], [143, 212], [143, 212], [143, 139], [143, 139], [143, 51], [143, 51], [149, 159], [149, 159], [149, 241], [149, 241], [161, 163], [161, 163], [161, 230], [161, 230], [161, 0], [161, 0], [199, 201], [199, 201], [199, 245], [199, 245], [199, 196], [199, 196], [209, 212], [209, 212], [209, 163], [209, 163], [382, 383], [382, 383], [382, 380], [382, 380], [471, 473], [471, 473], [471, 469], [471, 469], [471, 425], [471, 425], [481, 477], [481, 477], [481, 435], [481, 435], [506, 526], [506, 526], [506, 483], [506, 483], [0, 3], [13, 8], [27, 24], [76, 122], [76, 122], [94, 48], [139, 24], [163, 165], [177, 180], [388, 383], [453, 499], [526, 528], [526, 528], [3, 5], [48, 51], [48, 51], [122, 125], [180, 249], [180, 249], [383, 291], [505, 499], [5, 51], [125, 56], [125, 56], [202, 201], [499, 483], [51, 56], [362, 364], [362, 364], [483, 391], [483, 391], [364, 295], [245, 249], [245, 291], [245, 291], [245, 241], [245, 241], [295, 291], [295, 291], [291, 289], [90, 159], [90, 88], [90, 88], [205, 251], [205, 251], [251, 435], [435, 425], [435, 425], [108, 111], [108, 85], [88, 111], [108, 111], [230, 241], [230, 391], [230, 241], [241, 425], [425, 421], [469, 461], [263, 332], [263, 260], [377, 375], [377, 285], [328, 397], [328, 323], [328, 282], [303, 257], [303, 257], [395, 397], [401, 399], [401, 332], [282, 328], [285, 377], [375, 421], [375, 260], [397, 328], [399, 401], [421, 415], [332, 263], [415, 323], [260, 257], [323, 254], [323, 254]]

        self.assertEqual(138, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            results[i].sort()

        edges.sort()
        results.sort()
        self.assertListEqual(edges, results)

    def test_Case_Enonce(self):

        edges = APU.computeEdges("Projet_Cas_Enonce.txt")
        results=[[0, 2], [0, 2], [0, 3], [0, 3], [3, 4], [4, 5]]

        self.assertEqual(6, len(edges))
        for i in xrange(len(edges)):
            edges[i].sort()
            results[i].sort()

        edges.sort()
        results.sort()
        self.assertListEqual(edges, results)

if __name__ == '__main__':
    unittest.main()
