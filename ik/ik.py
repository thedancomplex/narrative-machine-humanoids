#!/usr/bin/env python

# File: t4.3-ik.py
# =======================
#
# Compute Inverse Kinematics
#
# Slide the end-effector forward and backward in the X-direction

from amino import SceneWin, SceneGraph, SceneIK, QuatTrans, YAngle, libamino
from math import pi
from time import sleep
import os
import sys

import rospy
from std_msgs.msg import Float32MultiArray

# Scene Parameters
# Change scene_plugin based on your directory structure
scene_plugin = sys.argv[1]
scene_name = sys.argv[2]
scene_ee = sys.argv[3]

pub = rospy.Publisher('musicSender', Float32MultiArray, queue_size=10)
rospy.init_node('robots', anonymous=True)

# Create an (empty) scene graph
sg = SceneGraph()

# Load the scene plugin
sg.load(scene_plugin, scene_name)

# Initialize the scene graph
sg.init()

# Create the sub-scenegraph from root to "hand"
ssg = sg[:scene_ee]

# Initialize and Start Window
win = SceneWin(scenegraph=sg, start=True, background=True)

# Create the inverse kinematics context
ik = SceneIK(ssg)

# IK Parameters
ik.set_seed_center()
ik.restart_time = 100e-3

# Set the reference transform
ik.ref_tf = (-0.199078, 0.678504, 0.199079, -0.678504), (-0.000000, -0.302836, 0.094977)

# Set the objective function
ik.set_obj(libamino.aa_rx_ik_opt_err_trans)

# Set the angle tolerance to be some big number

ik.set_tol_angle(100000)

dt = .1
period = 3
while win.is_runnining():
    # Solve IK
    print("solving ik\n")
    q_sub = ik.solve()

    # Display in Window
    if q_sub:  # check for valid solution
        print(list(q_sub))
        win.config = ssg.scatter_config(q_sub)
        pub.publish(data=q_sub)
    else:
        print("No IK Solution")

    # reseed for next run
    ik.set_seed_rand()

    # Sleep a bit
    t = 0
    while win.is_runnining() and t < period:
        sleep(dt)
        t += dt
