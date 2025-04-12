#!/bin/bash
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt
python main.py
