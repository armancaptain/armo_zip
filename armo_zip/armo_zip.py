import zipfile as zip
import os

os.chdir(r'c:\users\arman\Desktop' )
name=input("please enter zip name: ") + '.zip'
password=input("please enter password: ")
try: 
    myzip=zip.ZipFile(name)
    myzip.extractall(pwd=password.encode())
except:
        print(" ERORE ! can't extract this file. ")
