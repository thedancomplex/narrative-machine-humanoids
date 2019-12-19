#!/usr/bin/env python

# File: t4.1-fk.py
# =======================
#
# Compute Forward Kinematics

from amino import SceneWin, SceneGraph, SceneFK
from math import pi, cos
from time import sleep
import os
import sys

# Scene Parameters
# Change scene_plugin based on your directory structure
scene_plugin = sys.argv[1]

# Create an (empty) scene graph
sg = SceneGraph()

# Load the scene plugin
sg.load(scene_plugin, "darwin")
sg.load(scene_plugin, "music")
# Initialize the scene graph
sg.init()

# Create a window, pass the scenegraph, and start
print("creating window")
win = SceneWin(scenegraph=sg, start=True, background=True)

# Create the FK context
print("window created")
fk = SceneFK(sg)

# Do a simple wave
dt = 1.0 / 60
t = 0
config_dict = {
    "j_wrist_l": pi/2,
    "j_gripper_l": pi/2,
    "j_shoulder_l": pi/2,
}
while win.is_runnining():
    # update forward kinematics
    fk.config = config_dict

    # update window
    win.fk = fk

    # absolute hand pose is changing
    TF_g_h = fk["right_mallot"]
    print("g->mallot: %s" % TF_g_h)

    # sleep till next cycle
    sleep(dt)
    t += dt
