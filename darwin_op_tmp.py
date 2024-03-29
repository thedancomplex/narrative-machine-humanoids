#!/usr/bin/env python
# /* -*-  indent-tabs-mode:t; tab-width: 8; c-basic-offset: 8  -*- */
# /*
# Copyright (c) 2013, Daniel M. Lofaro
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the author nor the names of its contributors may
#       be used to endorse or promote products derived from this software
#       without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Based on: https://github.com/thedancomplex/pydynamixel
# */

import os
import dynamixel
import time
import random
import sys
import subprocess
import optparse
import yaml
import numpy as np
import PyCM730_h as cm

# Hubo-ach stuff
##import hubo_ach as ha
##import ach
from ctypes import *
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 8009

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def rad2dyn(rad):
    return np.int(np.floor( (rad + np.pi)/(2.0 * np.pi) * 4096 ))

def dyn2rad(en):
    return en / 4096.0 * 2.0 * np.pi - np.pi

def enable():
    cm730 = cm.CM730()
    cm730.connect()
    cm730.dxl_on()
    time.sleep(1)
#    cm730.check_ID(0, 255)
#    cm730.servo_sync_enable_torque([19, 20])
    cm730.disconnect()

def enable2(serial, net):
    myActuators = []
    for dyn in net.get_dynamixels():
        print dyn.id
        myActuators.append(net[dyn.id])

    myActuators.append(net[0x03])    
    if not myActuators:
      print 'No Dynamixels Found!'
      sys.exit(0)
    else:
      print "...Done"
    
    for actuator in myActuators:
#        actuator.synchronized = True
        actuator.torque_enable = True
    return 0 


def main(settings):
    # Open Hubo-Ach feed-forward and feed-back (reference and state) channels
#    s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
#    e = ach.Channel(ha.HUBO_CHAN_ENC_NAME)
#    r = ach.Channel(ha.HUBO_CHAN_REF_NAME)
    #s.flush()
    #r.flush()

    # feed-forward will now be refered to as "state"
#    state = ha.HUBO_STATE()

    # encoder channel will be refered to as "encoder"
#    encoder = ha.HUBO_ENC()

    # feed-back will now be refered to as "ref"
#    ref = ha.HUBO_REF()

    # Get the current feed-forward (state) 
#    [statuss, framesizes] = s.get(state, wait=False, last=True)
#    [statuss, framesizes] = e.get(encoder, wait=False, last=True)


    enable()

    portName = settings['port']
    baudRate = settings['baudRate']
    highestServoId = settings['highestServoId']

    # Establish a serial connection to the dynamixel network.
    # This usually requires a USB2Dynamixel
    serial = dynamixel.SerialStream(port=portName, baudrate=baudRate, timeout=1)
    net = dynamixel.DynamixelNetwork(serial)


    # Before search you must enable the dyn
    # This is untested but should turn the actuators on (i.e. the lights should blink once)
###    enable(serial,net)


    # Ping the range of servos that are attached
    print "Scanning for Dynamixels..."
    net.scan(1, highestServoId)

    myActuators = []

    for dyn in net.get_dynamixels():
        print dyn.id
        myActuators.append(net[dyn.id])

    if not myActuators:
      print 'No Dynamixels Found!'
      sys.exit(0)
    else:
      print "...Done"

    for actuator in myActuators:
        actuator.moving_speed = 50
        actuator.synchronized = True
        actuator.torque_enable = True
        actuator.torque_limit = 800
        actuator.max_torque = 800

# Set servo pos to 0.0

    state = 0
    while True:
	
       data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
       print "received message:", data
       # Get the current feed-forward (state) 
       #        [statuss, framesizes] = s.get(state, wait=False, last=True)
       if(str(data) == "H"):
	    state = 1
	    print("got it")
            for actuator in myActuators:
                actuator.goal_position = rad2dyn(0.0) # set all ids in range to 0.0 rad
                if (actuator.id == 5):
                    actuator.goal_position = rad2dyn(-3.14/2.0) # set id 5 to -pi/2 rad
                if (actuator.id == 6):
                    actuator.goal_position = rad2dyn(3.14/2.0) # set id 6 to  pi/2 rad
                if (actuator.id == 3):
                    actuator.goal_position = rad2dyn(3.14/4.0) # set id 3 to pi/4 rad
                if(actuator.id == 4):
                    actuator.goal_position = rad2dyn(-3.14/4.0) # set id 4 to -pi/4 rad
       elif(str(data[0]) == "M"):
            print("good")
            mot = int(data[1])
            print("motor: ",mot)
            if(data[2] == "A"):
                val = float(data[3:len(data)].decode())
                print("val: ",val)
		for actuator in myActuators:
		    if(actuator.id == mot):
		        actuator.goal_position = rad2dyn(val)
            elif(data[2] == "V"):
                vel = int(data[3:len(data)].decode())
                print(vel)
                for actuator in myActuators:
                    actuator.moving_speed = vel
       elif((data[0]) == "P"):
	    # send to robot 
            net.synchronize()

    

def validateInput(userInput, rangeMin, rangeMax):
    '''
    Returns valid user input or None
    '''
    try:
        inTest = int(userInput)
        if inTest < rangeMin or inTest > rangeMax:
            print "ERROR: Value out of range [" + str(rangeMin) + '-' + str(rangeMax) + "]"
            return None
    except ValueError:
        print("ERROR: Please enter an integer")
        return None
    
    return inTest

if __name__ == '__main__':
    
    parser = optparse.OptionParser()
    parser.add_option("-c", "--clean",
                      action="store_true", dest="clean", default=False,
                      help="Ignore the settings.yaml file if it exists and \
                      prompt for new settings.")
    
    (options, args) = parser.parse_args()
    
    # Look for a settings.yaml file
    settingsFile = 'settings.yaml'
    if not options.clean and os.path.exists(settingsFile):
        with open(settingsFile, 'r') as fh:
            settings = yaml.load(fh)
    # If we were asked to bypass, or don't have settings
    else:
        settings = {}
        if os.name == "posix":
            portPrompt = "Which port corresponds to your USB2Dynamixel? \n"
            # Get a list of ports that mention USB
            try:
                possiblePorts = subprocess.check_output('ls /dev/ | grep -i usb',
                                                        shell=True).split()
                possiblePorts = ['/dev/' + port for port in possiblePorts]
            except subprocess.CalledProcessError:
                sys.exit("USB2Dynamixel not found. Please connect one.")
                
            counter = 1
            portCount = len(possiblePorts)
            for port in possiblePorts:
                portPrompt += "\t" + str(counter) + " - " + port + "\n"
                counter += 1
            portPrompt += "Enter Choice: "
            portChoice = None
            while not portChoice:                
                portTest = raw_input(portPrompt)
                portTest = validateInput(portTest, 1, portCount)
                if portTest:
                    portChoice = possiblePorts[portTest - 1]

        else:
            portPrompt = "Please enter the port name to which the USB2Dynamixel is connected: "
            portChoice = raw_input(portPrompt)
    
        settings['port'] = portChoice
        
        # Baud rate
        baudRate = None
        while not baudRate:
            brTest = raw_input("Enter baud rate [Default: 1000000 bps]:")
            if not brTest:
                baudRate = 1000000
            else:
                baudRate = validateInput(brTest, 9600, 1000000)
                    
        settings['baudRate'] = baudRate
        
        # Servo ID
        highestServoId = None
        while not highestServoId:
            hsiTest = raw_input("Please enter the highest ID of the connected servos: ")
            highestServoId = validateInput(hsiTest, 1, 255)
        
        settings['highestServoId'] = highestServoId
        
        # Save the output settings to a yaml file
        with open(settingsFile, 'w') as fh:
            yaml.dump(settings, fh)
            print("Your settings have been saved to 'settings.yaml'. \nTo " +
                   "change them in the future either edit that file or run " +
                   "this example with -c.")
    
    main(settings)
