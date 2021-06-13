import json
import requests
from requests import exceptions
from requests import status_codes
from requests.api import get, head
from requests.models import Response
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from urllib3.exceptions import InsecureRequestWarning


APIC_URL = "https://devasc-aci-1.cisco.com"

def apic_login():
    """login to apic"""
    token = ""
    err = ""


    try:
        Response = requests.post(
            url = APIC_URL+"/api/aaaLogin.json",
            headers={
                "Content-Type": "application/json; charset = utf-8",
            },
            data=json.dumps(
                {
                    "aaaUser":{
                        "attributes":{
                            "name": 'devnetuser',
                            "pwd": "CardBoardGreen12!"
                        }
                    }
                }
            ),
            verify=False
        )
        json_reponse = json.loads(Response.content)
        token = json_reponse['imdata'][0]['aaaLogin']['attributes']['token']
        print (token)

        print ('response HTTP status Code: {status_code}'.format(status_code=Response.status_code))

    except requests.exceptions.RequestException as err:
        print ("http request failed")
        print (err)

    return token

def get_tenants():
    """get tenants"""

    token = apic_login()
    url=APIC_URL+"/api/node/class/fvTenant.json"
    print ('GET Request resource:', url)

    try:
        Response = requests.get(
            url,
            headers={
                "Cookie": "APIC-cookie=" + token,
                "Content-Type": "application/json; charset=utf-8",
            },
            verify=False
        )

        print ('Response HTTP Status Code: {status_code}'.format(status_code=Response.status_code))
        print ('response HTTP response Boday:', json.dumps(Response.json(), indent=4))
        
    except requests.exceptions.RequestException:
        print ("http request failed")

def get_devices():
    """ get devoces"""

    token = apic_login()
    url = APIC_URL+"/api/node/class/topology/pod-1/topSystem.json"
    print ('Get request resource:', url)

    try:
        response =requests.get(
            url,
            headers={
                "Cookie": "APIC-cookie=" + token,
                "Content-Type": "application/json; charset =utf-8"
            },
            verify=False
        )

        print ('Response HTTP status Code: {status_code}'.format(status_code=response.status_code))
        print ('Response HTTP response Body:', json.dumps(response.json(), indent=4))

    except requests.exceptions.RequestException:
        print("http request failed")

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


print('=========================GET TENANTS=======================')
get_tenants()
print('=========================GET DEVICES=======================')
get_devices()