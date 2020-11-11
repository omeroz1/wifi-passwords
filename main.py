import os
import shutil

"""
Author: Omer Oz
Date: 21/10/2020
Description: 
>>> the code collects all the names and passwords of the networks that was once connected to this device.
>>> you can view all the passwords of the wifis in the dictionary argument.
>>> to view the password of the network: print(dictionary[wifi_username])
>>> all of the wifi.xml files are located in 'C:/wifi_accounts' once the code is running at least once.
"""


def main():
    path = 'C:\\wifi_accounts'
    os.mkdir(path)
    os.system("netsh wlan export profile folder=C:\\wifi_accounts key=clear")
    arr_txt = [x for x in os.listdir('C:\\wifi_accounts') if x.endswith(".xml")]

    dictionary = {}

    for file in arr_txt:
        f = open(path + "\\" + file, "r")
        x = f.read()
        if '<keyMaterial>' in x:
            start_password = x.index('<keyMaterial>')
            finish_password = x.index('</keyMaterial>')
            tmp_password = (x[start_password + 13:finish_password])
            start_name = x.index('<name>')
            finish_name = x.index('</name>')
            tmp_name = (x[start_name + 6:finish_name])
            dictionary[tmp_name] = tmp_password
            f.close()

    print(dictionary)
    shutil.rmtree('/wifi_accounts')


if '__name__' == main():
    main()
