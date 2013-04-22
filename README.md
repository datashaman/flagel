flagel
======

Bottle / Knockout / Kickstart / RequireJS / CoffeeScript boilerplate

Installation
------------

Prerequisites:

*   Python 2.6+
*   Ruby 1.8.7+
*   rubygems
*   bundler gem
*   pip (usually installed with Python)

Install nodejs and npm (included with nodejs). Use the latest version from [nodejs.org]:

    wget http://nodejs.org/dist/v0.10.4/node-v0.10.4.tar.gz
    tar xvf node-v0.10.4.tar.gz
    cd node-v0.10.4/
    ./configure
    make
    sudo make install

Install bower globally with npm:

    sudo npm install -g bower

Create a virtualenv for the Python application (or not, your choice), and ensure you can run the python package manager *pip*.
Once your environment is activated, continue with the installation:

    make install
