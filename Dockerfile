FROM ros:kinetic

COPY . /narrative-machine-humanoids

RUN sudo apt-get update

RUN sudo apt-get install -y python3-pip nano

RUN pip3 install --upgrade pip

RUN pip3 install mido pyyaml rospkg
