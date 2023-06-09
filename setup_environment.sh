#!/bin/bash

# Update the system
sudo apt-get update
sudo apt-get upgrade

# Install dependencies for OpenCV
sudo apt-get install -y build-essential cmake pkg-config
sudo apt-get install -y libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libfontconfig1-dev libcairo2-dev
sudo apt-get install -y libgdk-pixbuf2.0-dev libpango1.0-dev
sudo apt-get install -y libgtk2.0-dev libgtk-3-dev
sudo apt-get install -y libatlas-base-dev gfortran
sudo apt-get install -y python3-dev

# Download OpenCV and OpenCV-contrib source files
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip

# Unzip the source files
unzip opencv.zip
unzip opencv_contrib.zip

# Create a build directory for OpenCV
cd opencv-4.5.0/
mkdir build
cd build/

# Configure and build OpenCV
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.5.0/modules \
      -D PYTHON_EXECUTABLE=$(which python3) \
      -D BUILD_EXAMPLES=ON ..

make -j4
sudo make install
sudo ldconfig

# Install TensorFlow
pip3 install tensorflow

# Install eSpeak
sudo apt-get install -y espeak

# Install Tesseract OCR
sudo apt-get install -y tesseract-ocr
sudo apt-get install -y libtesseract-dev

