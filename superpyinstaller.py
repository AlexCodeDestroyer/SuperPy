def superPyInstaller():
	import urllib.request
	import sys
	import os
	selfPath = os.getcwd()
	os.mkdir("/superpy/")
	url = "https://github.com/AlexCodeDestroyer/SuperPy/blob/master/superpy1.py"
	urllib.request.urlretrieve(url, "/superpy/superpy1.py")
	url = "https://github.com/AlexCodeDestroyer/SuperPy/blob/master/superpy2.py"
	urllib.request.urlretrieve(url, "/superpy/superpy2.py")
	url = "https://github.com/AlexCodeDestroyer/SuperPy/blob/master/superpy3.py"
	urllib.request.urlretrieve(url, "/superpy/superpy3.py")
	os.remove(selfPath + "\superpyinstaller.py")