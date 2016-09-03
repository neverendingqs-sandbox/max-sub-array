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
        self.testcases = []
        
        self.testcases.append({'input':[-2, 1, -3, 4, -1, 2, 1, -5, 4], 'index':3, 'length':4, 'sum':6})
        self.testcases.append({'input':[1, 2, 3, -7, 8, -1, 8], 'index':4, 'length':3, 'sum':15})
        self.testcases.append({'input':[1, 2, 3, -5, 8, -1, 8], 'index':0, 'length':7, 'sum':16})
        self.testcases.append({'input':[], 'index':0, 'length':0, 'sum':0})
        self.testcases.append({'input':[-5, -9, 0, -20], 'index':0, 'length':0, 'sum':0})
        self.testcases.append({'input':[-5, -9, -20], 'index':0, 'length':0, 'sum':0})
    
        pass

    def tearDown(self):
        pass


    def testKadane(self):
        for i in range(len(self.testcases)):
            self.assertEqual(self.array.kadane(self.testcases[i]['input']), self.testcases[i]['sum'])
        pass

    def testKadaneWithSubarray(self):
        for i in range(len(self.testcases)):
            expectedResults = self.testcases[i]['index'], self.testcases[i]['length'], self.testcases[i]['sum']
            actualResults = self.array.kadaneWithSubarray(self.testcases[i]['input'])
            self.assertEqual(expectedResults, actualResults)
        pass
    
    def testBruteForce(self):
        for i in range(len(self.testcases)):
            expectedResults = self.testcases[i]['index'], self.testcases[i]['length'], self.testcases[i]['sum']
            actualResults = self.array.bruteForce(self.testcases[i]['input'])
            self.assertEqual(expectedResults, actualResults)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()