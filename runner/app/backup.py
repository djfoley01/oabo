# Runner Pod
# The responsibility of this application is to run inside 
# a pod, executed as a cronjob inside of OpenShift.

import os
import subprocess
import requests
import json

def execute(namespace, deploymconfig, path):
	# Execute OpenShift Login
	cmda = ["oc", "login", os.environ["OCPURL"], "--token=" + os.environ["OCPTOKEN"]]
	login = subprocess.Popen(cmda, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Keep for Troubleshooting purposes
        oa, ea = login.communicate()
        print('Output: ' + oa.decode('ascii'))
        print('Error: ' + ea.decode('ascii'))
        print('code: ' + str(login.returncode))

	# Get POD name
	cmdb = ["oc", "get", "pods", "-n", namespace, "-l", "deploymentconfig=" + deploymconfig, "|", "grep", "-v", "NAME", "|", "awk", '"{', "print", '$1', '}"']
	#cmdb = ["oc", "get", "pods", "-n", namespace, "-l", "deploymentconfig=" + deploymconfig]
	pod = subprocess.Popen(cmdb, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Keep for Troubleshooting purposes
        ob, eb = pod.communicate()
        print('Output: ' + ob.decode('ascii'))
        print('Error: ' + eb.decode('ascii'))
        print('code: ' + str(pod.returncode))
	print(cmdb)
	
	# Execute OpenShift Command: oc rsync <pod-name>:<path> <localbackupDir> -n <namespace>
	cmdc = ["oc", "get", "pods", "-n", namespace]
	proc = subprocess.Popen(cmdc, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Keep for Troubleshooting purposes
	oc, ec = proc.communicate()
	print('Output: ' + oc.decode('ascii'))
	print('Error: ' + ec.decode('ascii'))
	print('code: ' + str(proc.returncode))

# Query the primary service orchestrating the backups
# The PODs name will change relatively frequently, so this
# application needs to query the primary service 

execute("home", "jenkins", "/home")


