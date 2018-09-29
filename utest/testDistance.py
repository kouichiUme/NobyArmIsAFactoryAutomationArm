#  -*- coding: UTF-8 -*-
import unittest
import sys
sys.path.append("..")
import Distance
class TestDistance(unittest.TestCase):

    def test_calcDistance(self):
            print("start move")
            dist = Distance.Distance()
            targetDist = [100,200,200]
            dist.calcDistanceBetween(targetDist)
            self.assertEqual("foo".upper(),"FOO")
        
if __name__ == '__main__':
    unittest.main()