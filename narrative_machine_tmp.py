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
NUM_JOINTS = 22

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

sp = np.zeros(NUM_JOINTS)
def set(mot, val):
  global sock,UDP_PORT_C,UDP_IP_C,state,sp
  sp[int(mot)] = val
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
  sock_B.close()
  sock_B = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  sock_B.bind((UDP_IP_B,UDP_PORT_B))
  data, addr = sock_B.recvfrom(1024)
  curBeat,subBeat,maxBeat = data.split(" ")
  

  return(int(curBeat),int(subBeat),int(maxBeat))
  #block until next beat
  #return an int as to where in the measure we are



def init(var=None):
 global myActuators,t,net,sock_C,sock_B,sock,UDP_IP_C,UDP_PORT_C,UDP_IP_B,UDP_PORT_B
 if(var == None):
  UDP_IP_B = "0.0.0.0"
  UDP_PORT_B = 8009

  UDP_IP_C = "127.0.0.1"
  UDP_PORT_C = 8010

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
  sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  sock_C = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
  sock_C.bind((UDP_IP_C, UDP_PORT_C))

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



def get(mot):
  global state, sp
  for i in range(NUM_JOINTS):
     state[i,pos] = state[i,ref]
  print state[int(mot),pos]
  #return state[int(mot),pos]
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print "#######################sp###################"
  print sp[int(mot)]
  return sp[int(mot)]
  #return(myActuators)
  # get current angle values of robot



RSP = 1
LSP = 2
REP = 5
LEP = 6
RSR = 3
LSR = 4
RHY = 7
LHY = 8
RHR = 9
LHR = 10
RHP = 11
LHP = 12
RKP = 13
LKP = 14
RAP = 15
LAP = 16
RAR = 17
LAR = 18
NKY = 19
NKP = 20


# 0 = current value
# 1 = offests
# 2 = dir
ref = 0
offset = 1
direction = 2
dyn_val = 3
pos = 4
state = np.zeros((NUM_JOINTS,5))

def doInitVals():
  global state
  print REP
  print int(REP)
  print offset
  print state 
  state[int(REP),offset] = -3.14/2.0
  state[REP,offset] = -3.14/2.0
  state[LEP,offset] =  3.14/2.0
  state[RSR,offset] =  3.14/4.0
  state[LSR,offset] =  -3.14/4.0


  for i in range(NUM_JOINTS):
    state[i,direction] = 1.0
  state[LSR,direction] = -1.0
  state[RSR,direction] = -1.0
  state[LEP,direction] = 1.0
  state[REP,direction] = -1.0
  state[LSP,direction] = 1.0
  state[RSP,direction] = -1.0
  state[LHY,direction] = -1.0
  state[RHY,direction] = -1.0
  state[RHR,direction] = -1.0
  state[LHR,direction] = -1.0
  state[RHP,direction] = 1.0
  state[RHP,direction] = -1.0
  state[RKP,direction] = 1.0
  state[LKP,direction] = -1.0
  state[RAP,direction] = -1.0
  state[LAP,direction] = 1.0
  state[RAR,direction] = 1.0
  state[LAR,direction] = 1.0
  state[NKY,direction] = 1.0
  state[NKP,direction] = -1.0
  
def setVals():
  global state
  print "setVals"
  for i in range(NUM_JOINTS):
    rad_tmp = state[i,ref]*state[i,direction] + state[i,offset]
    state[i,dyn_val] = rad2dyn(rad_tmp)

def setRef(i, val):
  global state, sp
  state[int(i),ref] = val
  sp[int(i)] = val
  print "setRef"
  print state[int(i),ref]
  setVals()


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
  global sock_C,myActuators,net,state
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
  loop_state = 0


  # Set State matrix
  doInitVals()
  setVals()
  try:
    while True:
	
       data, addr = sock_C.recvfrom(1024) # buffer size is 1024 bytes
       print "received message - dan:", data
       if(str(data) == "H"):
	    loop_state = 1
	    print("H - got it")
            for i in range(NUM_JOINTS):
                setRef(i,0.0)
            for actuator in myActuators:
                actuator.goal_position = rad2dyn(0.0) # set all ids in range to 0.0 rad
                actuator.goal_position = int(state[actuator.id,dyn_val]) 
       elif(str(data[0]) == "M"):
            print("M - good")
            mot = int(data[1])
            print("motor: ",mot)
            print(data[2])
            if(data[2] == "A"):
                print("MA - good")
                val = float(data[3:len(data)].decode())
                print("val: ",val)
		for actuator in myActuators:
		    if(actuator.id == mot):
                        print "ma good"
                        print state[actuator.id,ref]
                        setRef(int(actuator.id),val)
                        print "ma good 2"
                        print state[actuator.id,ref]
		        actuator.goal_position = int(state[actuator.id,dyn_val])
            elif(data[2] == "V"):
                print("V - good")
                vel = int(data[3:len(data)].decode())
                print(vel)
                for actuator in myActuators:
                    actuator.moving_speed = vel
            else:
                print("Else - good")
                mot = mot*10 + float(data[2])
                print("motor",mot)
                if(data[3] == "A"):
                    val = float(data[4:len(data)].decode())
                    print("val: ",val)
                    for actuator in myActuators:
                        if(actuator.id == mot):
                          setRef(actuator.id,val)
                          actuator.goal_position = int(state[actuator.id,dyn_val])
                elif(data[3] == "V"):
                    vel = int(data[4:len(data)].decode())
                    print(vel)
                    for actuator in myActuators:
                        actuator.moving_speed = vel

       elif((data[0]) == "P"):
	    # send to robot
            net.synchronize()
            for i in range(NUM_JOINTS):
              state[i,pos] = state[i,ref]

       elif((data[0]) == "E"):
            exit()
  except:
    print("Exit on error EXIT")
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
