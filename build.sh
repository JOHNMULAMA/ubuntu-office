#!/bin/bash

sudo apt update && sudo apt install -y python3-pip python3-venv libxcb-cursor0
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt