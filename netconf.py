from ncclient import manager
import xml.dom.minidom

#Courseware Cisco Devnet Sandbox
HOST = 'devasc-iosxe-mgmt-1.cisco.com'
USER = 'developer'
PASS = 'CactusMopedGreen42'
PORT = 830
#Filtering inteface GigabitEthernet1 Only
netconf_filter = """
<filter>
   <interfaces xmls="urn:ieft:params:xml:ns:yang:ietf-interfaces">
     <interface>
       <name>GigabitEthernet1</name>
     </interface>
   </interfaces>
</filter>
"""

#device is Cisco CSR
m = manager.connect(host=HOST, port=PORT, username=USER, password=PASS, hostkey_verify=False, device_params={'name': 'csr'})
reply = m.get_config(source='running', filter=netconf_filter)
#Pretty print the XML reply
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
m.close_session()

