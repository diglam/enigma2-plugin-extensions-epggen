#!/bin/bash

echo "New EPGgen directory..."
mkdir /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen

echo "Copying files for enigma2PC..."
cp -R ./locale /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen

cp -R ./plugin.png /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen

cp -R ./__init__.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen

cp -R ./plugin.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen

cp -R ./ui.py /usr/local/e2/lib/enigma2/python/Plugins/Extensions/EPGgen
