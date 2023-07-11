#!/bin/bash

function install(){
    python -m venv env
    source ./env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    python main.py join
}

function run() {
    source ./env/bin/activate
    python main.py
}

if [ ! -d env ]; then
    install
else
    run
fi
