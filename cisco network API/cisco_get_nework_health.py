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
def get_client_health(dnacip, headers, params):
    """
    Get Network Device Health API wrapper
    this function returns the response from a GET Network health request
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
    uri = "https://" + dnacip + "/dna/intent/api/v1/client-health"
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
#to the get network_devices health uri
params =""

resp =get_client_health(dnacip, headers, params)

print ("all client health: ", json.dumps(resp.json()["response"], indent=4))

