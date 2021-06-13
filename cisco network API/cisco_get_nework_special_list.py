import requests
from requests.api import get, head
from urllib3.exceptions import InsecureRequestWarning
import json
import sys

##### Cisco DNA Center URL and Authentication Credentials
# In a 'real' application, this information might be in a 'config.py' file
# to keep authentication and target information out of the primary logic

# - Authentication to DevAsc DNA Center
dnacip = "devasc-dnacenter-1.cisco.com"
username = "devnetuser"
password = "C!3c0d$Y"
###########

# define Authentication method
def get_X_auth_token(dnacip,username,password):
    """
    Authenticate to remote Cisco DNA Center
​
    Parameters
    ----------
    dnacip (str): dnac routable DNS address or ip
    username (str): dnac user name
    password (str): password
​
    Return:
    ----------
    str: dnac access token
    """
    # Supress credential warning for this exercise
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    # Authentication API full URI
    post_uri = "https://" + dnacip + "/dna/system/api/v1/auth/token"
    print ("\nAuthenticate: POST %s"%(post_uri))

    try:
          # verify - set to False to tell requests to NOT verify server's TLS certificate
        #  In production code this should be left to default to 'True'
        r = requests.post(post_uri, auth = (username,password), verify=False)
        return r.json()["Token"]
    except:
        # Something wrong, cannot get access token
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        
#Get Network Device API Wrapper
def get_network_device(dnacip, headers, params, modifier):
    """
    Get Network Device API wrapper
    this function returns the response from a GET Network Device request
    if Status = 200
    else it prints the Stutus and reponse and aborts.
    parameter
    --------------
    dnacip(str): dnac routable DNS address or IP
    header: headers for request
    params: parameters to be added to the GET request

    Return:
    ------------
    reponse
    """

    #get network device URI
    uri = "https://" + dnacip + "/dna/intent/api/v1/network-device" + modifier
    try:
        if params =="":
            print ("\n---\nGET %s"%(uri))
        else:
            print ("\n---\nGET %s?%s"%(uri, params))

        resp = requests.get(uri, headers=headers, params=params, verify=False)
        print (resp.status_code)
        return resp
    except:
        #failed to obtain access token
        print ("Status: %s"%resp.status_code)
        print ("respnose: %s"%resp.text)
        sys.exit()

#Authenticate to the Cisco DNA Center
#and ottain an authentication token
token =get_X_auth_token(dnacip, username, password)
print ("returned Authentication Token:", (token))

#assign the authentication token to a header key value pair
#x-auth-token ={{token}}
headers = {"x-auth-token": token}

#start by getting a count of all devices of all types known to the cisco dna center
#by appending "/count" to the get network_devices uri
params ="series=Cisco Catalyst 9300 Series Switches"
modifier = "/count"
resp =get_network_device(dnacip, headers, params, modifier)
switch_count = json.dumps(resp.json()["response"])
print ("Catalyst 9300 Switch count: ", switch_count)

#request a list of the cisco 9300 switches
#remove the '/count' modifier, but leave the filter in place
modifier = ""
resp = get_network_device(dnacip, headers, params, modifier)
print ("catalyst 9300 switch list:", json.dumps(resp.json()["response"], indent = 4))

#focus in on key information from these devices nd pull out just
# key identifying information such as device type, ID, serial number, and IPV4

json_resp = resp.json()["response"]

for i in range(0, int(switch_count)):
    print ("switch %d: type %s. serial number: %s. deviceId: %s. Mgmt IPv4: %s"%(i,json_resp[i]['type'], json_resp[i]['serialNumber'], json_resp[i]['id'], json_resp[i]['managementIpAddress']))

#finally , use each device ID to discover the VLAN associated to that switch
params =""

for i in range(0,int(switch_count)):
    modifier = "/" +json_resp[i]['id'] +"/vlan"
    resp = get_network_device(dnacip, headers, params, modifier)
    print ("device serial number %s is attahced to vlan:"%(json_resp[i]['serialNumber']))
    print (json.dumps(resp.json()["response"], indent=4))