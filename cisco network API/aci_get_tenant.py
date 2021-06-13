import json
import requests
import sys
from requests import exceptions
from urllib3.exceptions import InsecureRequestWarning

APIC_URL =  "https://devasc-aci-1.cisco.com"

def apic_login():
   """login to apic"""

   token = ""
   err = ""
  

    try:
       response =requests.post(
           url = APIC_URL + "/api/aaaLogin.json",
           headers = {"Content-Type": "application/json; charset =urf-8"
           },
           data = json.dumps(
               {
                   "aaaUser":{
                       "attributes": {
                           "name": "devnetuser",
                           "pwd": "CardBoardGreen12!"
                       }
                   }
               }
           ),
           verify=False
        )

        json_reponse = json.loads(response.content)
        token = json_reponse['imdata'][0]['aaaLogin']['attributes']['token']
        print (token)

        print ('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))

    except requests.exceptions.RequestException as err:
       print ("Http Request failed")
       print (err)

    return token


   