
import time
import requests
import pyodbc

# from util.constant import *

ip35  = '172.16.66.35'
ip51  = '172.16.98.51'
ip66  = '172.16.66.66'
ip149  = '172.16.66.149'
ip249  = '172.16.66.249'
ip241  = '172.16.66.241'

db262 = 'DB262'
usernamemcas = 'mcas'
password = 'Bdclab123'

url = 'http://{}/PIsys/Sector/Sector.asmx'
operatorTag = '000'
serialNumber = '2129133568'
nationality = 'USA'
regionTag = 'zz'
productTagList1 = '1'
productTagList2 = '2'
refreshSectorCreate = '1'
locationTag = ''
headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}

body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <createSector xmlns="http://irdeto.com/pisys/sector">
      <operatorTag>{}</operatorTag>
      <serialNumber>{}</serialNumber>
      <nationality>{}</nationality>
      <regionTag>{}</regionTag>
      <productTagList>
        <string>{}</string>
      </productTagList>
    </createSector>
  </soap12:Body>
</soap12:Envelope>"""
sn_list = None
smsoperator_list = None
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+ip66+';DATABASE='+db262+';UID='+usernamemcas+';PWD='+ password)
# cursor = cnxn.cursor()

# cursor.execute("SELECT * FROM CaSMSOperator")
# cascrow = cursor.fetchall()

# # cursor.execute("SELECT * FROM [CaClientDevice]")
# # cascrow = cursor.fetchall()
# if len(cascrow):
#   smsoperator_list = []
#   for i in cascrow:
#     smsoperator_list.append(str(i[0]))


# cursor.execute("select * from casc;")
# cascrow = cursor.fetchall()


# for i in cascrow:
#     sn_list.append(str(i[1]))
  
# for i in sn_list:
#     response = requests.post(url=url.format(ip35), data=body.format(operatorTag, i, serialNumber,nationality, regionTag, productTagList1), headers=headers)
#     time.sleep(2)
#     print(i)
#     print(response.reason)
#     print(response)
#     print(response.text)
#     print(type(response.text))


class CONNECTION:
    def __init__(self, server, db_name, db_user, db_password, odbc_driver_version=None):
        self.server = server
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.odbc_driver_version = odbc_driver_version
        self._check_driver()

        try:
            self.cnxn = pyodbc.connect(self.DRIVER + self.SERVER + \
                        self.DATABASE + self.USERNAME + self.PASSWORD)
        except Exception:
            self.__exit__(sys.exc_info())

        self.cursor = self.cnxn.cursor()   
    
    def _check_driver(self) -> None:
        if self.odbc_driver_version is None:
            tmp = []
            for i in pyodbc.drivers():
                # if 'ODBC Driver 17' in i or 'ODBC Driver 13' in i:
                if 'ODBC Driver' in i:
                    tmp.append(int(i[11:14]))
            if max(tmp) == 17:
                self.odbc_driver_version = 17
            elif max(tmp) == 13:
                self.odbc_driver_version = 13
            else:
                self.odbc_driver_version = int(tmp.max()[:-2])

    def _connect(self):
        if self.odbc_driver_version == 17:
            try:
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                    +self.server
                                    +';DATABASE='
                                    +self.db_name
                                    +';UID='
                                    +self.db_user
                                    +';PWD='
                                    +self.db_password)
                print('db connection setup successfully')
                return cnxn
            except Exception as e:
                print(e)
                print('db connection setup failed')
        elif self.odbc_driver_version == 13:
            try:
                cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                                +self.server
                                +';DATABASE='
                                +self.db_name
                                +';UID='
                                +self.db_user
                                +';PWD='
                                +self.db_password)               
                print('db connection setup successfully')
                return cnxn
            except Exception as e:
                print(e)
                print('db connection setup failed')
        else:
            print('unkonw odbc_driver_version')
    
    def db_execute(self, command):
        _cursor = self._connect().cursor()
        try:
            _cursor.execute(command)
        except Exception as identifier:
            print(identifier)
            print('db execute failed')
        # _cursor.execute(command)
        return _cursor

    def db_fetch_all(self):
        return self.db_execute().fetchall()

    def db_fetch_one(self):
        return self.db_execute().one()

    def db_close(self):
        self._connect().close()

db_command = "SELECT * FROM CASC"
    
my_connect = CONNECTION(ip66, db262, usernamemcas, password)
my_connect.db_execute(db_command)

for i in my_connect.db_fetch_all():
    print(i)
# print()
my_connect.db_close()

# cursor.execute("select * from casmartcardsector;")
# casmartcardsector_row = cursor.fetchall()

# active_list = []

# for i in casmartcardsector_row:
#     active_list.append(str(i[0]))

# for i in cascrow:
#     response = requests.post(url=url.format(ip35), data=body.format(operatorTag, str(i[1]), serialNumber,nationality, regionTag, productTagList1), headers=headers)
#     time.sleep(2)
#     print(response.reason)
#     print(response)

# for i in cascrow:
#     if str(i[0]) not in active_list:
#         print(str(i[1]))
#         response = requests.post(url=url.format(ip35), data=body.format(operatorTag, str(i[1]),nationality, regionTag, productTagList1), headers=headers)
#         time.sleep(2)
#         print(response.reason)
#         print(response)
#         time.sleep(1)
