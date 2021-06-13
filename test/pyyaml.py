# Fill in this file with the code from parsing YAML exercise

import json
import yaml

yaml_file = open("./test/myfile.yml","r")

pythondata = yaml.safe_load(yaml_file)

print(pythondata['expires_in'])

print("The access token from YAML is: %s" % pythondata['access_token'])

print("\n\n")

print(json.dumps(pythondata))