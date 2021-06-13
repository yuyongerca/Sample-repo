#the request library is userd to communicate with vmanage.
import requests
#pprint is used to make the output more readable. it is mainly used for
#illustration, but is also used for debuging and verbose presendtation.
import pprint
import urllib3

#disable_warning from urllib3 disables the warning from using the self-singned
#certificate used in vManage by default
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#this is the information that we need to get to vManage and authenticate. Although
#the port can be assumed, the suername and password is needed to get an API token.
vmanage_host = 'devasc-sdwan-1.cisco.com'
vmanage_port = '443'
vmanage_username ='devnetuser'
vmanage_pasword = 'RE!_Yw519_27'

#the base url is simply the vManage's IP address/hostname is URL format with 
#optional port number
base_url = 'https://%s:%s'%(vmanage_host, vmanage_port)

#the session token is retrieved from the path '/j_security_check'. Since we are using
#the requests library, the token is added to subsequent calls
login_action = '/j_security_check'

#the suername and password are pased in as part of the payload of the API call.
login_data ={'j_username': vmanage_username, 'j_password':vmanage_pasword}


#combining the base URL with the path renders the end point from when we get
#and API token
login_url =base_url+ login_action

#create the requests session object
session = requests.session()

#we make a POST call of the URL and data from above. if the response is in 
#HTML, it means that a login error has occurred
login_response = session.post(url=login_url, data=login_data, verify=False)
if b'<html>' in login_response.content:
    print ("Login failed")
    exit(1)


#the XSRF Token is used to prevent cross-ste request forgery attacks and is
#rquired in vManaged 19.x
xsrf_token_url = base_url + '/dataservice/client/token'
print (xsrf_token_url)

#now GET the URL constructed above to retrieve the token. If a successful
#return code is not recevied (i.e.200), then an error was encountered
login_token = session.get(url=xsrf_token_url,verify=False)
if login_token.status_code == 200:
    if b'<html>' in login_token.content:
        print ("Login Token Failed")
        exit(1)

    session.headers['X-XSRF-TOKEN'] = login_token.content

device_url = base_url + '/dataservice/device'

device_list = session.get(url=device_url, verify=False)
if device_list.status_code == 200:
    json_data = device_list.json()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json_data)

else:
    print (device_list.status_code)
    exit(1)
    