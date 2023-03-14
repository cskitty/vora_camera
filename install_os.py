#!/bin/bash

# Download the Raspbian image
curl -OL https://downloads.raspberrypi.org/raspbian_lite_latest

# Unzip the image
unzip raspbian_lite_latest

# Get the name of the image file
IMAGE_FILE=$(ls | grep ".img" | head -1)

# Get the name of the disk
DISK=$(diskutil list | grep "external, physical" | grep -o "disk[0-9]")

# Unmount the disk
diskutil unmountDisk /dev/$DISK

# Write the image to the disk
sudo dd bs=1m if=$IMAGE_FILE of=/dev/r$DISK

# Eject the disk
diskutil eject /dev/$DISK

