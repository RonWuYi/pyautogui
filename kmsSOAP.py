
import time
import requests
import pyodbc

from util.constant import *

ip35  = '172.16.66.35'
ip51  = '172.16.98.51'
ip149  = '172.16.66.149'
ip249  = '172.16.66.249'
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

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server35+';DATABASE='+database+';UID='+usernamemcas+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("select * from casc;")
cascrow = cursor.fetchall()
sn_list = []

for i in cascrow:
    sn_list.append(str(i[1]))
  
for i in sn_list:
    response = requests.post(url=url.format(ip35), data=body.format(operatorTag, i, serialNumber,nationality, regionTag, productTagList1), headers=headers)
    time.sleep(2)
    print(i)
    print(response.reason)
    print(response)
    print(response.text)
    print(type(response.text))

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
