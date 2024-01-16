#!/bin/bash

function install(){
    python3 -m pip install --user --upgrade pip
    python3 -m pip install --user virtualenv
    python3 -m venv env
    source ./env/bin/activate
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    python3 main.py join_to_chats
}

function run() {
    while true
    do
        source ./env/bin/activate
        python3 main.py anon3.session
        # python3 main.py ya.session
        sleep 3600
    done
}

if [ ! -d env ]; then
    install
else
    run
fi
