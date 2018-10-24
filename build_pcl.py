#!/usr/bin/env python3
'''

Build and install a local version of lib pcl in ENAC's classrooms

'''

import os, shutil
import urllib.request
import pdb

INSTALL_ROOT='/home/personnel/SINA/Drouinan/local_pcl' #/src/enac_stuff'/media/commun_mialp_eleves'
BUILD_ROOT='/tmp/build_drouin'
DOWNLOAD_ROOT='/tmp/download_drouin'

def clean_filesystem(clean_dl, clean_build, clean_install):
    for d, f in zip((DOWNLOAD_ROOT, BUILD_ROOT, INSTALL_ROOT),
                    (clean_dl, clean_build,  clean_install)):
        if f:
            try:  
                print ("Deleting {}".format(d))
                shutil.rmtree(d)
            except OSError as e:  
                print ("Deletion of {} failed ()".format(d, e))

def create_filesystem():
    for d in (DOWNLOAD_ROOT, BUILD_ROOT, INSTALL_ROOT):
        try:
            os.mkdir(d)
            print ("created {}".format(d))
        except FileExistsError:
            print (" {} exists, not creating".format(d))


def _system(cmd):
    print('executing: {}'.format(cmd))
    os.system(cmd)


class Eigen:
    dl_url = 'http://bitbucket.org/eigen/eigen/get/3.3.5.tar.gz'
    dl_target = os.path.join(DOWNLOAD_ROOT, 'eigen_3.3.5.tar.gz')

    def install():
        os.chdir(BUILD_ROOT)
        _system('tar xf {}'.format(Eigen.dl_target))
        SRC_ROOT = BUILD_ROOT+'/eigen-eigen-b3f3d4950030'
        os.chdir(SRC_ROOT); os.mkdir('build'); os.chdir(SRC_ROOT+'/build')
        _system('cmake -DCMAKE_INSTALL_PREFIX:PATH={} ..'.format(INSTALL_ROOT))
        _system('make'); _system('make install')


class Flann:
    dl_url = 'http://www.cs.ubc.ca/research/flann/uploads/FLANN/flann-1.8.4-src.zip'
    dl_target = os.path.join(DOWNLOAD_ROOT, os.path.basename(dl_url))

    def install():
        '''
        Python and Matlab binding are not built - needed? venv?
        '''
        os.chdir(BUILD_ROOT)
        _system('unzip {}'.format(Flann.dl_target))
        SRC_ROOT = BUILD_ROOT+'/flann-1.8.4-src'
        os.chdir(SRC_ROOT); os.mkdir('build'); os.chdir(SRC_ROOT+'/build')
        cmake_options  = '-DBUILD_MATLAB_BINDINGS=OFF -DBUILD_PYTHON_BINDINGS=OFF'
        cmake_options += ' -DCMAKE_INSTALL_PREFIX:PATH={}'.format(INSTALL_ROOT)
        cmake_cmd = 'cmake {} ..'.format(cmake_options) 
        _system(cmake_cmd)
        _system('make'); os.system('make install')       


class Vtk:
    dl_url = 'https://www.vtk.org/files/release/8.1/VTK-8.1.1.tar.gz'
    dl_target = os.path.join(DOWNLOAD_ROOT, os.path.basename(dl_url))
    
    def install():
        os.chdir(BUILD_ROOT)
        _system('tar xf {}'.format(Vtk.dl_target))
        SRC_ROOT = BUILD_ROOT+'/VTK-8.1.1'
        os.chdir(SRC_ROOT); os.mkdir('build'); os.chdir(SRC_ROOT+'/build')
        _system('cmake -DCMAKE_INSTALL_PREFIX:PATH={} ..'.format(INSTALL_ROOT))
        _system('make'); _system('make install')

        
class Qhull:
    dl_url = 'http://www.qhull.org/download/qhull-2015-src-7.2.0.tgz'
    dl_target = os.path.join(DOWNLOAD_ROOT, os.path.basename(dl_url))
    
    def install():
        os.chdir(BUILD_ROOT)
        _system('tar xf {}'.format(Qhull.dl_target))
        os.chdir(BUILD_ROOT+'/qhull-2015.2/build')
        _system('cmake -DCMAKE_INSTALL_PREFIX:PATH={} ..'.format(INSTALL_ROOT))
        _system('make'); _system('make install')

# class Metslib:
#     dl_url = 'http://www.coin-or.org/download/source/metslib/metslib-0.5.3.tgz'
#     dl_target = os.path.join(DOWNLOAD_ROOT, os.path.basename(dl_url))

#     def install():
#         os.chdir(BUILD_ROOT)
#         _system('tar xf {}'.format(Metslib.dl_target))
#         os.chdir(BUILD_ROOT+'/metslib-0.5.3')
#         _system('./configure --prefix=/home/personnel/SINA/Drouinan/local_pcl')
#         _system('make install')
        
class Pcl:
    dl_url = 'https://github.com/PointCloudLibrary/pcl/archive/pcl-1.8.1.tar.gz'
    dl_target = os.path.join(DOWNLOAD_ROOT, os.path.basename(dl_url))

    def install():
        os.chdir(BUILD_ROOT)
        _system('tar xf {}'.format(Pcl.dl_target))
        SRC_ROOT = BUILD_ROOT+'/pcl-pcl-1.8.1'
        os.chdir(SRC_ROOT); os.mkdir('build'); os.chdir(SRC_ROOT+'/build')
        cmake_options  = ' -DCMAKE_INSTALL_PREFIX:PATH={}'.format(INSTALL_ROOT)
        #cmake_options += ' -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON'
        cmake_options += ' -DBUILD_visualization=ON'
        cmake_options += ' -DBUILD_examples=OFF'
        _system('cmake {} ..'.format(cmake_options))
        _system('make'); _system('make install')

        
        #cmake .. -DEIGEN_INCLUDE_DIR=/home/personnel/SINA/Drouinan/src/eigen3 -DCMAKE_INSTALL_PREFIX:PATH=/home/personnel/SINA/Drouinan/local_pcl_install  -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DBUILD_visualization=on -DQHULL_INCLUDE_DIR=PATH=/media/commun_mialp_eleves/ASNAT/local_pcl_install/include



        
        
def download(c, force=False):
    if force or not os.path.isfile(c.dl_target):
        print('Downloading {} to {}'.format(c.dl_url, c.dl_target))
        urllib.request.urlretrieve(c.dl_url, c.dl_target)
    else:
        print('{} exists, not downloading'.format(c.dl_target))
        
def install(c):
    print('Installing {}'.format(c.__name__))
    c.install()
        
def main():
    clean_filesystem(clean_dl=False, clean_build=False, clean_install=False)
    create_filesystem()
    for c in [Eigen, Flann, Vtk, Qhull]: c.ignore = True
    for c in [Eigen, Flann, Vtk, Qhull, Pcl]:
        print('### {} ###'.format(c.__name__))
        if hasattr(c, 'ignore'):
            print('  ignoring')
        else:
            download(c)
            install(c)

    
if __name__ == "__main__":
    main()
