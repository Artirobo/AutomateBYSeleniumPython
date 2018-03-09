from distutils.core import setup
#install pip install  py2exe_py2  for windowsn and for ubuntu pip install py2exe
import py2exe

# to  run the setup file  
#run by this comman  in windows : python setup.py py2exe
#in helloworld you can set any files

setup(console=['helloworld.py'])

