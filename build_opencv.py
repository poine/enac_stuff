#!/usr/bin/env python3
'''

Build and install a local version of opencv in ENAC's classrooms

'''
import os, sys, shutil, urllib.request, pdb

DOWNLOAD_ROOT='/tmp/download_drouin'
BUILD_ROOT='/tmp/build_drouin'

def _system(cmd):
    print('executing: {}'.format(cmd))
    os.system(cmd)
    
def main():
    dl_url = 'https://github.com/opencv/opencv/archive/3.4.3.tar.gz'
    dl_target = os.path.join(DOWNLOAD_ROOT, 'opencv_3.4.3.tar.gz')
    #urllib.request.urlretrieve(dl_url, dl_target)    
    dl2_url = 'https://github.com/opencv/opencv_contrib/archive/3.4.3.tar.gz'
    dl2_target = os.path.join(DOWNLOAD_ROOT, 'opencv_contrib_3.4.3.tar.gz')
    #urllib.request.urlretrieve(dl2_url, dl2_target)
    os.chdir(BUILD_ROOT)
    #_system('tar xf {}'.format(dl_target))
    #_system('tar xf {}'.format(dl2_target))
    BUILD_DIR = os.path.join(BUILD_ROOT, 'opencv_build')
    _system('mkdir {}'.format(BUILD_DIR))
    os.chdir(BUILD_DIR)
    cmake_cmd =  'PKG_CONFIG_PATH=/home/personnel/SINA/Drouinan/local_pcl/share/pkgconfig:/home/personnel/SINA/Drouinan/local_pcl/lib/pkgconfig/'
    cmake_cmd += ' cmake -DCMAKE_BUILD_TYPE=RELEASE'
    cmake_cmd += ' -D CMAKE_INSTALL_PREFIX=/home/personnel/SINA/Drouinan/local_opencv'
    cmake_cmd += ' -D INSTALL_PYTHON_EXAMPLES=ON'
    cmake_cmd += ' -D INSTALL_C_EXAMPLES=OFF'
    cmake_cmd += ' -D OPENCV_EXTRA_MODULES_PATH=/tmp/build_drouin/opencv_contrib-3.4.3/modules'
    cmake_cmd += ' -D BUILD_EXAMPLES=ON'
    cmake_cmd += ' ../opencv-3.4.3'
    #_system(cmake_cmd)
    _system('make')
    #cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/home/personnel/SINA/Drouinan/opencv_user2 -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_C_EXAMPLES=OFF -D OPENCV_EXTRA_MODULES_PATH=/tmp/aruco_build/opencv_contrib-3.3.0/modules -D BUILD_EXAMPLES=ON ../opencv-3.3.0

    

if __name__ == "__main__":
    main()
