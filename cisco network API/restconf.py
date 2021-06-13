import requests
import sys
import json
from urllib3.exceptions import InsecureRequestWarning

HOST = 'ios-xe-mgmt.cisco.com:9443'
USER = 'developer'
PASS = 'C1sco12345'

#Disable SSL Warning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Basic Auth is used for authentication
def get_configured_intefaces(interface):
    """Retrieving config data (interface) from RESTCONF api."""
    api = "/restconf/data/ietf-interfaces:interfaces/interface="+interface
    url = "https://"+HOST+api
    print (url)
    #RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+jason',
                'Accept': 'application/yang-data+jason'}
    #this statement performs a GET on the specified url
    response =requests.get(url, auth=(USER, PASS), headers=headers, verify=False)
    print ("Status code:", response.status_code)
    if response.status_code == 200:
        #return JSON
        return response
    else:
        return None
def main():
    """Simple main method calling function"""
    interface ="GigabitEthernet1"
    interfaces = get_configured_intefaces(interface)
    #print JSON that is returned
    if interfaces != None:
        response_json = interfaces.json()
        print ("Response:", json.dumps(response_json,indent = 4))
    else:
        print ("Looks like " + interface +"is not configured!!!")

if __name__ == '__main__':
    sys.exit(main())