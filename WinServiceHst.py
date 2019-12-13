# plan to use windows service start HST, but failed, this is not allowed on windows.

import time
import sys
import socket
import psutil
import win32event
import win32service
import servicemanager
import win32serviceutil

from requests import put, get
from datetime import datetime
my_app = "C:\\Users\\hdc\\Downloads\\CloakedCAAgent_4.11.1_InteractiveClient_2019-05-13-11-33-07\\CloakedCAHst.exe"

# import os


PROCNAME = "CloakedCAHst.exe"

# if os.path.exists(my_app):
#     print("yes")
# else:
#     print("no")

def check_running():
    if "CloakedCAHst.exe" in (p.name() for p in psutil.process_iter()):
        # print("running")
        put('http://localhost:5000/todo1', data={'data': f'{datetime.now}'}).json()
    else:
        # print("not running")
        import os
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
        # if "CloakedCAHst.exe" in (p.name() for p in psutil.process_iter()):
                proc.kill()
        if "CloakedCAHst.exe" in (p.name() for p in psutil.process_iter()):
            for proc in psutil.process_iter():
                if proc.name() == PROCNAME:
        # if "CloakedCAHst.exe" in (p.name() for p in psutil.process_iter()):
                    proc.kill()
        else:
            os.system(f'start {my_app}')


class TestService(win32serviceutil.ServiceFramework):
    _svc_name_ = "TestService"
    _svc_display_name_ = "Test Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            # with open('C:\\TestService.log', 'a') as f:
            #     f.write('test service running...\n')
            check_running()
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)
            time.sleep(5)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(TestService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(TestService) 
