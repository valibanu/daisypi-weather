echo "Welcome to the 'Daisy Pi Weather Station Project' installer"
echo "Installing the required packages ..."

echo "Installing pip (Python Package Manager) ..."
#apt-get install -q -y python-pip
apt-get -q -y install python-setuptools
easy_install pip
echo "Finished installing pip!"

cho "Installing the supervisor tool ..."
apt-get -q -y install supervisor
echo "Finished installing supervisor!"

echo "Installing python-smbus ..."
apt-get -q -y install python-smbus
echo "Finished installing python-smbus!"

echo "Installing the Raspberry Pi GPIO Python package ..."
sudo apt-get -q -y install python-rpi.gpio
echo "Finished installing python-rpi.gpio!"

echo "Installing the Python package for reading SHT1X ..."
easy_install -U distribute
pip install rpiSht1x
echo "Finished installing rpiSht1x!"

echo "Installing the Xively Python package ..."
pip install --pre xively-python
echo "Finished installing xively-python"

echo "Getting some additional help from Adafruit ..."
mkdir Adafruit_BMP085
cd Adafruit_BMP085
wget https://raw.github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/master/Adafruit_BMP085/Adafruit_BMP085.py
wget https://raw.github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/master/Adafruit_I2C/Adafruit_I2C.py
touch __init__.py
cd ..
#git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
echo "Finished fetching all of the requirements!"

echo "Enabling i2c ..."
sed -i.bak 's/^blacklist i2c-bcm2708/\ #blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
echo "i2c-dev" | sudo tee -a /etc/modules
echo "Done"
echo "Please reboot the system!"

