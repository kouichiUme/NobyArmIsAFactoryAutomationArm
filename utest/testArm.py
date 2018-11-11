#  -*- coding: UTF-8 -*-
import unittest
import sys
sys.path.append("..")
import math
import Arm
class TestArm(unittest.TestCase):

    def test_move(self):
            self.assertEqual("foo".upper(),"FOO")
        
    def test_hogehoge(self):
        arm = Arm.Arm();
        locationXyz = [1,2,3]
        self.assertEqual("move x:" + str(1) +" y: "+str(2)+" z: "+ str(3),arm.move(locationXyz));

    def test_calc(self):
        arm = Arm.Arm();
        arm.calc()
        self.assertFalse(False);


    def test_calcLocationFromThetas(self):
        arm = Arm.Arm();
        thetas = [0,0,0,0,0,3.14/4]
        arm.calcPositionFromAngles(thetas);

    def test_calcTargetDirection(self):
        arm = Arm.Arm()
        targetXyz= [-1,0,1]
        self.assertAlmostEqual(math.pi/4,arm.calcDirectionFromTarget(targetXyz))

if __name__ == '__main__':
    unittest.main()