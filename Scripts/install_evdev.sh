#!/bin/bash
# install_evdev.sh
# Moves python-evdev files from Scripts/python/evdev to /usr/lib/python3.9/site-packages/evdev/
sudo mkdir -p /usr/lib/python3.9/site-packages/evdev
sudo mv Scripts/python/evdev/* /usr/lib/python3.9/site-packages/evdev/
sudo chmod -R 755 /usr/lib/python3.9/site-packages/evdev
sudo mv /usr/lib/python3.9/lib-dynload/libevdev.so /usr/lib/python3.9/lib-dynload/libevdev.so.bak 2>/dev/null || true
echo "python-evdev installed to /usr/lib/python3.9/site-packages/evdev/"
