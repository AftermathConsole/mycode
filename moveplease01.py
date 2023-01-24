#!/usr/bin/env python3

#import tools needed for operation
import shutil
import os

# for directoy to start in
os.chdir('/home/student/mycode/')

# call shutil.move to move the file.
shutil.move('raynor.obj', 'ceph_storage/')

#watch out that if the file already exists in the destination, it will be overwriten.

# prompt user for a new name for the kerrigan.obj file

xname = input("What is the new name for kerrigan.obj? ")

# rename file with the new name from the user input
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)


