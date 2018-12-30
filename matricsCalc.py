import numpy as np
import math
import Arm 


#腕移動計算　
# 軸計算
# 1     0           0               0
# x     cos(theta1) -sin(theta1)    0
# y     sin(theta1) cos(theta1)     0
# z     0           0               1
def transportXyzAxisZ(x,y,z,theta1):
    return np.matrix([[1,0,0,0],[x,math.cos(theta1),-math.sin(theta1),0],[y,math.sin(theta1),math.cos(theta1),0],[z,0,0,1]])


#腕移動計算　
# 軸計算
# 1     0           0               0
# x     cos(theta1) 0               -sin(theta1)
# y     0           1               0
# z     sin(theta1) 0               cos(theta1)
def transportXyzAxisY(x,y,z,theta1):
    return np.matrix([[1,0,0,0],[x,math.cos(theta1),0,-math.sin(theta1)],[y,0,1,0],[z,math.sin(theta1),0,math.cos(theta1)]])


#腕移動計算　
# 軸計算
# 1     0           0               0
# x     1           0               0
# y     0           cos(theta1)     -sin(theta1)
# z     0           sin(theta1)     cos(theta1)
def transportXyzAxisX(x,y,z,theta1):
    return np.matrix([[1,0,0,0],[x,1,0,0],[y,0,math.cos(theta1),-math.sin(theta1)],[z,0,math.sin(theta1),math.cos(theta1)]])






print(np.dot(3,3))

# 回転行列を初期化する
def makeTransposeMatrix(a,b,c,d,e,f,g,h,i,x,y,z):
    return np.matrix([[1,0,0,0],[x,a,d,g],[y,b,e,h],[z,c,f,i]])

#
a = makeTransposeMatrix(1,0,0,0,1,0,0,0,1,0,0,1)
t1 = transportXyzAxisZ(1,0,0,math.pi/2)
t2 = transportXyzAxisY(0,1,0,math.pi/2)
t3 = transportXyzAxisX(0,0,1,math.pi/2)


print(a)
inva = np.linalg.inv(a)



print("-- inv a -- ")
print(inva)
#逆行列をかける

e = np.matmul(a,inva)
print("-- a a_ -- ")
print(e)
# 1,1要素のarc cos の値をとる
print(math.acos(a.item((1,1))))
print(math.acos(a.item((1,2))))



print("print t1")

print(t1)
iT1 = np.linalg.inv(t1)
print("-- inv t1 --")
print(iT1)

e2 = np.matmul(t1,iT1)
print("--e2--")
print(e2)


print("--t2--")
print(t2)
#逆行列をもとめる
iT2 = np.linalg.inv(t2)
print("-- inv t2 --")
print(iT2)
e3 = np.matmul(t2,iT2)
print(e3)

# t3 
print("-- t3 --")
print(t3)
# 逆行列
iT3 = np.linalg.inv(t3)
print("-- inv t3 --")
print(iT3)
e3  = np.matmul(t3,iT3)
# 逆行列かける行列
print(e3)

# Y軸に沿って math.pi /2 回転
#  
# t1 * (0,0,-1)から(1,0,0)になるはず
rotateTable = transportXyzAxisY(0,0,0,math.pi/2)
print(" 0,0,-1 を回転")
act = np.matmul(rotateTable,[1,0,0,-1])
print(act)

# Y軸に沿って移動して
# y軸に回転しているからY自体は変更されない
translateY = transportXyzAxisY(0,1,0,math.pi/2)
actYaxismove = np.matmul(translateY,[1,0,0,-1])
print(actYaxismove)

# X軸に沿って回転
rotateT2 = transportXyzAxisX(0,0,0,math.pi/2)
actXaxisRotate = np.matmul(rotateT2,[1,0,1,0])
# 0,0,1になるはず
print(actXaxisRotate)

#todo 残りの３軸に対して移動


# Z軸に沿って回転
rotateT3 = transportXyzAxisZ(0,0,0,math.pi/2)
# 肩から先の腕の部分です
actZaxisRotate = np.matmul(rotateT3,[1,0,1,0])
#[1,-1,0,0]になるはず
print('rotate axis z [1,-1,0,0]')
print(actZaxisRotate)



