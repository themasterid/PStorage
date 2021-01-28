# PStorage
PStorage - A program for storing information in electronic form. 
MySQL is protected by a key, you will not be able to view it. 
To create a database, use your key to decrypt the data in the database.

Work in Windows 10 x64. and Linux Mint 20 x64!
 
For compile sqlcipher in Windows 10 and install pysqlcipher3 in system pip see this readme:

1. Install python 3.6 x64 or x86.

2. Install Win64 OpenSSL v1.1.1i or Win32 OpenSSL v1.1.1i: https://slproweb.com/products/Win32OpenSSL.html
in C:\OpenSSL-Win64 or C:\OpenSSL-Win64 directory.

3. Add in use Visual Studio 2019 Developer Command Prompt v16.8.4 (menu - x86 Native Tools Command Prompt for VS 2019) this

   for x86:
```
SET OPENSSL_CONF=C:\OpenSSL-Win32\bin\openssl.cfg
```
   or for x64:
```
SET OPENSSL_CONF=C:\OpenSSL-Win64\bin\openssl.cfg
```
   and for x86: 
```
set LIB=C:\OpenSSL-Win32\lib;%LIB%
set INCLUDE=C:\OpenSSL-Win32\include;%INCLUDE%
```
   or for x64:
```
set LIB=C:\OpenSSL-Win64\lib";%LIB%
set INCLUDE=C:\OpenSSL-Win64\include";%INCLUDE%
```
4. Install ActiveTcl from https://www.activestate.com/products/tcl/.

5. Install Visual Studio 2019 for build sqlite3.c sources.

6. Clone SQLCipher from GitHub use Visual Studio 2019 Developer Command Prompt v16.8.4 (menu - x86 Native Tools Command Prompt for VS 2019):
```
mkdir SQLCipher
cd SQLCipher
git clone https://github.com/sqlcipher/sqlcipher.git
cd C:\Users\broot\Documents\GitHub\SQLCipher\sqlcipher
cd sqlcipher
nmake /f Makefile.msc clean
nmake /f Makefile.msc
```
The final compilation will report an error, it's does not matter, just copy sqlite3.c, sqlite3.h files.
```
cd ..
git clone https://github.com/rigglemania/pysqlcipher3.git
cd pysqlcipher3
mkdir amalgamation
cd amalgamation
mkdir sqlcipher
cd ..
```
put in /amalgamation, /amalgamation/sqlcipher and /sqlcipher/sqlcipher folders this sqlite3.c, sqlite3.h files.

Example:

- SQLCipher/pysqlcipher3/amalgamation
	- sqlite3.c
	- sqlite3.h
- SQLCipher/pysqlcipher3/amalgamation/sqlcipher
	- sqlite3.c
	- sqlite3.h
	
- SQLCipher/pysqlcipher3/sqlcipher/sqlcipher
	- sqlite3.c
	- sqlite3.h

Go to directory /SQLCipher/pysqlcipher3

And in Native Tools Command Prompt for VS 2019 run:
```
>python setup.py build_amalgamation
-----------------------------------------------
running build_amalgamation
Builds a C extension using a sqlcipher amalgamation
building 'pysqlcipher3._sqlite3' extension
...
Creating library build\temp.win-amd64-3.6\Release\src\python3\_sqlite3.cp36-win_amd64.lib and object build\temp.win-amd64-3.6\Release\src\python3\_sqlite3.cp36-win_amd64.exp
Generating code
Finished generating code
-----------------------------------------------
```
   (if you see: 
```fatal error C1083: Cannot open include file: 'openssl/rand.h': No such file or directory```
   )

   try done in point 3.

7. Next step, Native Tools Command Prompt for VS 2019 run:
```
python setup.py install
-----------------------------------------------
running install
running bdist_egg
running egg_info
writing pysqlcipher3.egg-info\PKG-INFO
writing dependency_links to pysqlcipher3.egg-info\dependency_links.txt
...
...
...
Installed c:\users\__YOURUSER__\appdata\local\programs\python\python36\lib\site-packages\pysqlcipher3-1.0.3-py3.6-win-amd64.egg
Processing dependencies for pysqlcipher3==1.0.3
Finished processing dependencies for pysqlcipher3==1.0.3
-----------------------------------------------
```

7. Try run this commands in cmd:
```
pip list
Package                   Version
------------------------- ------------
...
pysqlcipher3              1.0.3
...
```
```
python -V
Python 3.6.0
```
```
'python'
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from pysqlcipher3 import dbapi2 as sqlite3
>>>
```
Its work! :)
