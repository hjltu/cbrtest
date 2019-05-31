#!/bin/bash

# tested on Ubuntu 18.04 x64
echo "usage:
# bash run.sh [-env, -i]
# -env: create virtual environment
# -i: install behave and selenium"

export VENV="venv"

if [ $1 ]; then
    # install env
    if [ $1 == "-env" ]; then
        echo "*** INSTALL ENV ***"
        virtualenv -p python3 $VENV
    fi

    # install app
    if [ $1 == -i ]; then
        echo "*** INSTALL ***"
        $VENV/bin/pip install behave selenium
    fi
fi

# start
if [ -z $1 ]; then
    echo "*** START ***"
    $VENV/bin/behave
fi

echo "*** END TEST ***"
sleep(2)

# send email
# first check the required fields in myemail.py file
MAIL="example@mail"
echo "*** SEND EMAIL TO $MAIL ***"
#python3 myemail $MAIL
echo "*** THE END ***"
