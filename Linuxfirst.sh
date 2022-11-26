echo "Installing the modules that are needed"

echo "Installing pip"
sudo apt install pip

echo "Checking if Python 3 is installed"
if [[ "$(python3 -V)" =~ "Python 3" ]]:
    echo ok no need to install

    echo installing tkinter
    pip install tkinter
    pip install tk
else:
    sudo apt-get update
    sudo apt-get install python3.6


    echo installing tkinter
    pip install tkinter
    pip install tk

echo "Running"
/bin/python3 main.py