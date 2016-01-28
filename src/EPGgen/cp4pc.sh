#!/bin/bash

echo "New EPGregen directory..."
mkdir /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

echo "Copying files for enigma2PC..."
cp -R ./locale /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

cp -R ./plugin.png /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

cp -R ./__init__.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

cp -R ./plugin.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

#cp -R ./ui.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen

#cp -R ./fn.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGregen
