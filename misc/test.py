import urllib3
import os
import requests
import json
#import yaml

urllib3.disable_warnings()

def get_pod_list(namespace):
        auth_token = os.environ['OCPTOKEN']
        url = os.environ['OCPURL']+"/api/v1/namespaces/" + namespace + "/pods"
        header = {"Authorization": "bearer " + auth_token}
        response = requests.get(url,headers=header,verify=False)
        if(response.ok):
                pv_list = json.loads(response.content)
                return json.dumps(pv_list, sort_keys=True, indent=4)
        else:
                return response.raise_for_status()

def get_projects():
        auth_token = os.environ['OCPTOKEN']
        url = os.environ['OCPURL']+"/api/v1/namespaces"
        header = {"Authorization": "bearer " + auth_token}
        response = requests.get(url,headers=header,verify=False)
        if(response.ok):
                project_list = json.loads(response.content)
                name = []
                items = project_list['items']
                for item in items:
                        name.append(item['metadata']['name'])

                return json.dumps(name, sort_keys=True, indent=4)
        else:
                return response.raise_for_status()

def get_pod_detail(deploymconfig):
        auth_token = os.environ['OCPTOKEN']
        url = os.environ['OCPURL']+"/api/v1/pods?labelSelector=deploymentconfig=" + deploymconfig
        header = {"Authorization": "bearer " + auth_token}
        response = requests.get(url,headers=header,verify=False)
        if(response.ok):
                pod_dtls = json.loads(response.content)
                return json.dumps(pod_dtls, sort_keys=True, indent=4)
        else:
                return response.raise_for_status()

def get_dc():
        auth_token = os.environ['OCPTOKEN']
        url = os.environ['OCPURL']+"/apis/apps.openshift.io/v1/deploymentconfigs"
        header = {"Authorization": "bearer " + auth_token}
        response = requests.get(url,headers=header,verify=False)
        if(response.ok):
                dc_list = json.loads(response.content)
                name = []
                vol_list = []
                vol_name = []
                vol_path = []
                items = dc_list['items']
                for item in items:
                        name.append(item['metadata']['name'])
                        vol_list = item['spec']['template']['spec']['containers'][0]
                        for vol in vol_list.get('volumeMounts', []):
                              vol_name.append(vol['name'])
                              vol_path.append(vol['mountPath'])

                return json.dumps(vol_name, sort_keys=True, indent=4)
                #return vol_list2.keys()
        else:
                return response.raise_for_status()

#def get_dc_yaml():
#        auth_token = os.environ['OCPTOKEN']
#        url = os.environ['OCPURL']+"/apis/apps.openshift.io/v1/deploymentconfigs"
#        header = {"Authorization": "bearer " + auth_token, "Accept": "application/yaml", "Content-Type": "application/yaml"}
#        response = requests.get(url,headers=header,verify=False)
#        if(response.ok):
#                dc_list = yaml.load(response.content)
#                name = []
#                vol_list = []
#                vol_name = []
#                vol_path = []
#                items = dc_list['items']
#                for item in items:
#                        name.append(item['metadata']['name'])
#                        vol_list = item['spec']['template']['spec']['containers'][0]
                        #vol_list2 = json.loads(vol_list)
#                        for vol in vol_list.get('volumeMounts', []):
#                              vol_name.append(vol['name'])
#                              vol_path.append(vol['mountPath'])
#
#                return yaml.dump(vol_name + vol_path)
#                #return vol_list2.keys()
#        else:
#                return response.raise_for_status()

def get_pv_list():
	auth_token = os.environ['OCPTOKEN']
	url = os.environ['OCPURL']+'/api/v1/persistentvolumes'
	header = {"Authorization": "bearer " + auth_token}
	response = requests.get(url,headers=header,verify=False)
	if(response.ok):
		pv_list = json.loads(response.content)
		name = []
		status = []
		size = []
		share = []
		server = []
		claim = []
		items = pv_list['items']
		for item in items:
			name.append(item['metadata']['name'])
			status.append(item['status']['phase'])
			if 'nfs' not in item['spec']:
				share.append("volumeid")
				server.append("EC2")
				continue
			share.append(item['spec']['nfs']['path'])
			server.append(item['spec']['nfs']['server'])
			size.append(item['spec']['capacity']['storage'])
			if 'claimRef' not in item['spec']:
				claim.append("None")
				continue
			claim.append(item['spec']['claimRef']['name'])

		return json.dumps(name, sort_keys=True, indent=4)
	else:
		return response.raise_for_status()

#output = get_pod_list("default")
#output = get_pv_list()
#output = get_projects()
#output = get_dc()
#output = get_dc_yaml()
output = get_pod_detail("jenkins")
print(output)
