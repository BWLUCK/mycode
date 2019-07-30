#!/usr/bin/python3
import shutil
import os
os.chdir("/home/student/mycode/")
shutil.move("raynor.obj", "ceph_storage/")
# The following line will rename the file
xname = input("What is the new name for kerrigan.obj file?")
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)
