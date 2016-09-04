'''
Created on Jun 22, 2013
Uses the unittest library to run tests on different implementations of the maxsubarray problem

@author: yunyun
'''

import unittest
from maxsubarray import maxsubarray

class maxsubarrayTests(unittest.TestCase):
    
    def setUp(self):
        self.array = maxsubarray()
        self.testcases = [
            {'input':[-2, 1, -3, 4, -1, 2, 1, -5, 4], 'index':3, 'length':4, 'sum':6},
            {'input':[1, 2, 3, -7, 8, -1, 8], 'index':4, 'length':3, 'sum':15},
            {'input':[1, 2, 3, -5, 8, -1, 8], 'index':0, 'length':7, 'sum':16},
            {'input':[], 'index':0, 'length':0, 'sum':0},
            {'input':[-5, -9, 0, -20], 'index':0, 'length':0, 'sum':0},
            {'input':[-5, -9, -20], 'index':0, 'length':0, 'sum':0}
        ]

        pass

    def tearDown(self):
        pass


    def test_kadane(self):
        for test_case in self.testcases:
            with self.subTest(test_case=test_case):
                expected_results = test_case['sum']
                actual_results = self.array.kadane(test_case['input'])
                self.assertEqual(expected_results, actual_results)

    def test_kadane_with_subarray(self):
        for test_case in self.testcases:
            with self.subTest(test_case=test_case):
                expected_results = test_case['index'], test_case['length'], test_case['sum']
                actual_results = self.array.kadaneWithSubarray(test_case['input'])
                self.assertEqual(expected_results, actual_results)
    
    def test_brute_force(self):
        for test_case in self.testcases:
            with self.subTest(test_case=test_case):
                expected_results = test_case['index'], test_case['length'], test_case['sum']
                actual_results = self.array.bruteForce(test_case['input'])
                self.assertEqual(expected_results, actual_results)

if __name__ == "__main__":
    unittest.main()
