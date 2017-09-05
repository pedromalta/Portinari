<p align="center">
  <img src="https://github.com/pedromalta/PortinariPhotos/raw/master/Front%20Gate%20Controller/20170830_141147.jpg" alt="Front gate controller."/>
</p>

# Appliances Controller
Little Python Script for exposing the appliances connected to the RaspBerry GPIO over the local network through a Web Api.

Place the Python script ``appliances.py`` on an "appliances" folder inside your home folder ``/home/pi``

Install supervisor with:
``sudo apt-get install supervisor``

place the ``appliances.conf`` file inside the ``/etc/supervisor/conf.d/``
