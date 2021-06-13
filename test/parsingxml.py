
import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()
ns = re.match(r'{.*}', root.tag).group(0)
print (ns)
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find(f"{ns}test-option")

print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testop.text)
