#!/bin/bash

function install(){
    python -m venv env
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
}

function run() {
    source ./env/bin/activate
    python main.py
}

if [ ! -d "$env"]; then
    install
fi

run
