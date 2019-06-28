@echo off
REM Batch command to easily invoke the pip install/ uninstall function.
REM User can quickly install the required python module by just entering the module name
REM Runs on Windows
 
:start
cls
echo.
echo.
echo Select menu
echo ================
echo 1. Display python modules being installed using pip function
echo 2. Pip installation (individual files)
echo 3. Pip install virtualenv and wapper
echo 4. Pip uninstall
echo.
 
REM set the python version here
set python_ver=36-32
 
set /p x=Pick:
IF '%x%' == '1' GOTO NUM_1
IF '%x%' == '2' GOTO NUM_2
IF '%x%' == '3' GOTO NUM_3
IF '%x%' == '4' GOTO NUM_4
GOTO start
 
:NUM_1
cd \
cd \python%python_ver%\Scripts\
pip freeze
pause
exit
 
:NUM_2
echo  Enter a filename to start install using pip
set INPUT=
set /P INPUT=Type input:%=%
 
cd \
cd \python%python_ver%\Scripts\
pip install %INPUT%
 
pause
exit

:NUM_3
cd \
cd \python%python_ver%\Scripts\
pip install virtualenv
pip install virtualenvwrapper-win

pause
exit

:NUM_4
echo  Enter a filename to UNINSTALL using pip
set INPUT=
set /P INPUT=Type input:%=%
 
cd \
cd \python%python_ver%\Scripts\
pip uninstall %INPUT%
 
pause
exit

