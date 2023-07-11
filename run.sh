#!/bin/bash

function install(){
    python3 -m venv env
    source ./env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 main.py join
}

function run() {
    source ./env/bin/activate
    python3 main.py
}

if [ ! -d env ]; then
    install
else
    run
fi
