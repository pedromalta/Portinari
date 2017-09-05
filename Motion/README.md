# Motion

This is the configuration for the Video Stream

Install Motion with ``sudo apt-get install motion``

Config Motion with ``nano /etc/motion/motion.conf`` the configuration depends on your setup but be sure to find the ``Live Stream Server`` preferences and set:

``stream_maxrate 30``

``stream_localhost off``

So that you can see the stream on another device and it doesn't lag.

To make it start on the boot sequence use: 

``sudo systemctl enable motion``
``sudo update-rc.d motion defaults``

and edit the file ``sudo nano /etc/defaults/motion`` setting daemon to yes ``start_motion_daemon=yes``

To check the stream access ``http://localhost:8081`` on the RaspBerry browser or ``http://[ip]:8081`` on another device.
