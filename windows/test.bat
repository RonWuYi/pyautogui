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
echo 3. Pip uninstall
echo.
 
REM set the python version here
set python_ver=36
 

cd \
dir
pause
exit