def set(mot, val):
# Set motor and angle value for joint
# Ready to be sent (but not sent)

def put():
# put all set values on to the robot

def get():
# get current angle values of robot

def init():
# initilize the dyn package
# also initializes network settings

def close():
# stops the dyn packs

def home():
# sets robot to home position

def vel(mot,vel):
# set velocity for mot at vel(deg/sec)

def beat():
# block until next beat
# return an int as to where in the measure we are

