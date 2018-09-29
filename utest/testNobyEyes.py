#  -*- coding: UTF-8 -*-
import sys
import unittest

import NobyEyes
import Distance
sys.path.append("..")
class TestNobyEyes(unittest.TestCase):

    def test_meatureDistance(self):
            print("detect start")
            ne =NobyEyes.NobyEyes()
            dis =    ne.meatureDistance()
            # 腕からの距離計算する
            dist= Distance.Distance()
            dist.calcDistanceBetween(dis)
            self.assertEqual("foo".upper(),"FOO")
        
if __name__ == '__main__':
    unittest.main()
