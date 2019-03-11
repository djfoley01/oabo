# Runner Pod
# The responsibility of this application is to run inside 
# a pod, executed as a cronjob inside of OpenShift.

import os
import subprocess
import requests
import json
import tarfile

def make_tarfile(output_filename, source_dir)
	with tarfile.open(output_filename, "w:gz") as tar:
		tar.add(source_dir, arcname=os.path.basename(source_dir))
	tar.close()

def execute(namespace, deploymconfig, path):
	# Execute OpenShift Login
	cmda = ["oc", "login", os.environ["OCPURL"], "--token=" + os.environ["OCPTOKEN"], "--insecure-skip-tls-verify=true"]
	login = subprocess.Popen(cmda, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Keep for Troubleshooting purposes
        oa, ea = login.communicate()
        print('Output: ' + oa.decode('ascii'))
        print('Error: ' + ea.decode('ascii'))
        print('code: ' + str(login.returncode))

	# Get POD name
	cmdb1 = ["oc", "get", "pods", "-n", namespace, "-l", "deploymentconfig=" + deploymconfig]
	cmdb2 = ["grep", "-v", "NAME"]
	cmdb3 = ["awk", '{ print $1 }']
	#cmdb = ["oc", "get", "pods", "-n", namespace, "-l", "deploymentconfig=" + deploymconfig]
	pod1 = subprocess.Popen(cmdb1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	pod2 = subprocess.Popen(cmdb2, stdin=pod1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	finalpod = subprocess.Popen(cmdb3, stdin=pod2.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Keep for Troubleshooting purposes
        ob, eb = finalpod.communicate()
        print('Output: ' + ob.decode('ascii'))
        print('Error: ' + eb.decode('ascii'))
        print('code: ' + str(finalpod.returncode))
	
	# Execute OpenShift Command: oc rsync <pod-name>:<path> <localbackupDir> -n <namespace>
	cmdc = ["oc", "rsync", "-n", namespace, ob.decode('ascii').rstrip() + ":" + path, "/home/daniel/backups/"]
	proc = subprocess.Popen(cmdc, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Keep for Troubleshooting purposes
	oc, ec = proc.communicate()
	print('Output: ' + oc.decode('ascii'))
	print('Error: ' + ec.decode('ascii'))
	print('code: ' + str(proc.returncode))

# Query the primary service orchestrating the backups
# The PODs name will change relatively frequently, so this
# application needs to query the primary service 

execute("home", "jenkins", "/var/jenkins_home")


