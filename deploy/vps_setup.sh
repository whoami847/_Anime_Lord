#!/bin/bash
apt update && apt upgrade -y
apt install python3 python3-pip -y
pip3 install -r requirements.txt
nohup python3 main.py &
