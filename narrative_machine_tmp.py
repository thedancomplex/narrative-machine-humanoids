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
import threading

# Hubo-ach stuff
##import hubo_ach as ha
##import ach
from ctypes import *
import socket

def home():
  global sock,UDP_IP_C,UDP_PORT_C
  toSend = "H"
  # sets robot to home position
  sock.sendto(toSend,(UDP_IP_C, UDP_PORT_C))

def vel(mot,vel):
  global sock,UDP_IP_C,UDP_PORT_C
  toSend = "M"+ str(mot) + "V" + str(vel).encode()
  sock.sendto(toSend,(UDP_IP_C, UDP_PORT_C))
  # set velocity for mot at vel(deg/sec)

def set(mot, val):
  global sock,UDP_PORT_C,UDP_IP_C
  # val is float to represent the joint angle in radians
  toSend = "M"+str(mot) + "A" + str(val).encode()
  sock.sendto(toSend,(UDP_IP_C, UDP_PORT_C))
  # Set motor and angle value for joint
  # Ready to be sent (but not sent)

def put():
  global sock,UDP_IP_C,UDP_PORT_C
  toSend = "P"
  sock.sendto(toSend,(UDP_IP_C,UDP_PORT_C))
  # put all set values on to the robot

def beat():
  global sock_B
  data, addr = sock_B.recvfrom(1024)
  curBeat,maxBeat = data.split(" ")
  

  return(int(curBeat))
  #block until next beat
  #return an int as to where in the measure we are



def init(var):
 global myActuators,t,net,sock_C,sock_B,sock,UDP_IP_C,UDP_PORT_C,UDP_IP_B,UDP_PORT_B
 if(var == None):
  UDP_IP_B = "0.0.0.0"
  UDP_PORT_B = 8009

  sock_C = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  sock_C.bind((UDP_IP_C, UDP_PORT_C))
  sock_B = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  sock_B.bind((UDP_IP_B,UDP_PORT_B))
  sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  return 0
 elif(var == 'server'):
  parser = optparse.OptionParser()
  parser.add_option("-c", "--clean",
                      action="store_true", dest="clean", default=False,
                      help="Ignore the settings.yaml file if it exists and \
                      prompt for new settings.")

  (options, args) = parser.parse_args()
  UDP_IP_C = "127.0.0.1"
  UDP_PORT_C = 8010


  maxBeat = 0
  curBeat = 0
  # Look for a settings.yaml file
  settingsFile = 'settings.yaml'
  if not options.clean and os.path.exists(settingsFile):
      with open(settingsFile, 'r') as fh:
          settings = yaml.load(fh)
  
  enable()

  portName = settings['port']
  baudRate = settings['baudRate']
  highestServoId = settings['highestServoId']
  # Establish a serial connection to the dynamixel network.
  # This usually requires a USB2Dynamixel
  serial = dynamixel.SerialStream(port=portName, baudrate=baudRate, timeout=1)
  net = dynamixel.DynamixelNetwork(serial)
  print "Scanning for Dynamixels..."
  net.scan(1, highestServoId)

  myActuators = []
  for dyn in net.get_dynamixels():
    print dyn.id
    myActuators.append(net[dyn.id])

  if not myActuators:
    print 'No Dynamixelis Found!' 
    return 1
    sys.exit(0)
  else:
    print "...Done"

  for actuator in myActuators:
    actuator.moving_speed = 50
    actuator.synchronized = True
    actuator.torque_enable = True
    actuator.torque_limit = 800
    actuator.max_torque = 800
  t=threading.Thread(target=main,args=(settings,))
  t.start()
  return 0
 else:
  return 1
def get():
  return(myActuators)
  # get current angle values of robot

"""
def close():
  # stops the dyn packs

"""

def doubleArms():
  vel(0,1023)
  i=0
  while(i < 3):
    set(2,-3.14/2.0)
    set(1,-3.14/2.0)
    set(5,0.0)
    set(6,0.0)
    put()
    time.sleep(1.0)
    set(5,-3.14/2.0)
    set(6,3.14/2.0)
    set(1,3.14/2.0)
    set(2,3.14/2.0)
    put()
    time.sleep(1.0)
    i+=1


def rad2dyn(rad):
    return np.int(np.floor( (rad + np.pi)/(2.0 * np.pi) * 4096 ))

def dyn2rad(en):
    return en / 4096.0 * 2.0 * np.pi - np.pi

def enable():
    global myActuators
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

def todoTasks():
    global maxBeat,curBeat
    init()
    vel(0,1023)
    count = 0
    while(count < 16):
        cur = beat()
        if(cur == 1):
             set(5,-3.14/4.0)
        elif(cur == 2):
             set(6,3.14/4.0)
        elif(cur == 3):
             set(1,3.14/4.0)
        elif(cur ==4 ):
             set(2,3.14/4.0)
        put()
        time.sleep(0.5)
        home()
        put()
        count += 1
        #if(int(curBeat) == int(maxBeat)):
        #    break
    home()
    put()

def nmexit():
  global t,sock,UDP_IP_C,UDP_PORT_C
  sock.sendto("E",(UDP_IP_C,UDP_PORT_C))
  t.join()
  exit()

def main(settings):
  global sock_C,myActuators,net
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



  #t = threading.Thread(target=todoTasks)
  #t.start()
  state = 0
  try:
    while True:
	
       data, addr = sock_C.recvfrom(1024) # buffer size is 1024 bytes
       print "received message:", data
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
            print(data[2])
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
            else:
                mot = mot*10 + float(data[2])
                print("motor",mot)
                if(data[3] == "A"):
                    val = float(data[4:len(data)].decode())
                    print("val: ",val)
                    for actuator in myActuators:
                        if(actuator.id == mot):
                            actuator.goal_position = rad2dyn(val)
                elif(data[3] == "V"):
                    vel = int(data[4:len(data)].decode())
                    print(vel)
                    for actuator in myActuators:
                        actuator.moving_speed = vel

       elif((data[0]) == "P"):
	    # send to robot 
            net.synchronize()
       elif((data[0]) == "E"):
            exit()
  except:
    print("EXIT")
    exit()
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
