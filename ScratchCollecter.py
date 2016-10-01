"""Mock up for Scratch projects recollector"""

import os
import requests
import datetime
import time
import json

def readJson (pid):
    """Get the json file of pid Scratch project"""

    api = "http://projects.scratch.mit.edu/internalapi/project/" + pid + "/get/"
    response = requests.get(api)
    if response.status_code == 200:
        return response.json()
    else:
        #FIXME: we should also write error message in log file
        return None

def writeJson (pid, data):
    """Write the data contents into a file in the folder for pid project"""
    file = pid + "/json.txt"
    with open(file, 'w') as outfile:
        if data is not None:
            json.dump(data, outfile)

def downloadSb2 (pid):
    """Get the sb2 file of the pid Scratch project"""
    #FIXME Instead of using the Heroku getsb2 demo, we should install ours
    getsb2 = "wget http://getsb2.herokuapp.com/" + pid
    os.system (getsb2)
    date = str(datetime.datetime.now()).replace(" ", "-")
    os.system ("mv " + pid + ".1" +  " " + pid + "/" + pid + "-" + date + ".sb2")


projects = [[20954379, "NULL" ], [16099065, "NULL"], [119472191, "NULL"]]

while True:
    for project in projects:
        pid = str(project[0])
        if project[1] == "NULL":
            os.system("mkdir " + pid)
            data = readJson(pid)
            writeJson(pid, data)
            downloadSb2(pid)
            project[1] = str(datetime.datetime.now()).replace(" ", "-")
        else:
            data = readJson(pid)
            with open(pid + "/json.txt") as old_file:    
                data_old = json.load(old_file)
            if data != data_old:
                writeJson(pid, data)
                project[1] = str(datetime.datetime.now()).replace(" ", "-")
                downloadSb2(pid)
    time.sleep(5)
