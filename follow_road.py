import time
import numpy as np
import math
import matplotlib.pyplot as plt

def turn_right() :
    speed_right=-50
    speed_left=50
    print('right')

def turn_left() :
    speed_right=50
    speed_left=-50
    print('left')






    
# def kinematics(S,vl,vr,t) :
#     l=120
#     R=l/2*(vr+vl)
#     omega=(vr-vl)/l
#     ICC=np.array([S[0]-R*np.sin(S[2]),S[1]+R*np.cos(S[2])])
#     rmat=np.array([ [np.cos(omega*t),-np.sin(omega*t),0],
#                     [np.sin(omega*t),np.cos(omega*t),0],
#                     [0,0,1]   ])
#     iccorg=np.transpose(np.array([S[0]-ICC[0],S[1]-ICC[1],S[2]]))
#     trsl=np.transpose(np.array(np.concatenate((ICC,[omega*t]))))
#     return np.matmul(rmat,iccorg)+trsl

def kinematics2(pose,vl,vr,dt) :
    x=pose[0]
    y=pose[1]
    theta=pose[2] 
    THYMIO_WHEELBASE=95
    dl = vl*dt/200
    dr = vr*dt/200
       
    dtheta = (dr-dl)/THYMIO_WHEELBASE
    dc = (dl+dr)/2
    
    x += dc*math.cos(theta + dtheta/2)
    y += dc*math.sin(theta + dtheta/2)
    theta += dtheta
    theta %= 2*math.pi

    return [x,y,theta]



def follow_path(traj) :
    #get position
    
    #get next point
    
    #get direction
    
    #call pid
    
    #
    print()

def theta_des(pos,obj) :
    return math.atan2(obj[1]-pos[1],obj[0]-pos[0])

def speed_des(pos,obj) :
    coeff=10
    return 500+coeff*math.sqrt((obj[1]-pos[1])**2+(obj[0]-pos[0])**2)

def wheel_inputs(omega,v) :
    R=30
    L=95
    return [(2*v-omega*L)/(2*R),(2*v+omega*L)/(2*R)]

def dist(v1,v2) :
    return math.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)


