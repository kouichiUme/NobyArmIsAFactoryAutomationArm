#  -*- coding: UTF-8 -*-
import unittest
import sys
sys.path.append("..")
import Arm
class TestArm(unittest.TestCase):

    def test_move(self):
            self.assertEqual("foo".upper(),"FOO")
        
    def test_hogehoge(self):
        arm = Arm.Arm;
        self.assertEqual("move x:" + str(1) +" y: "+str(2)+" z: "+ str(3),arm.move(1,2,3));

if __name__ == '__main__':
    unittest.main()