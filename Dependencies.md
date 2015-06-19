# Introduction #
The 16bit TIFF images provided by gdem is a format rather uncommon, in order to read them a proper package and libraries must be installed.

# Details #
At first we must download and install scikits-image packages for python from the git repository

git clone https://github.com/scikits-image/scikits-image

then libfreeimage


sudo apt-get install libfreeimage3 libfreeimage-dev

then

cd scikits-image/

sudo python setup.py install