#!/usr/bin/env python3
import json
from pprint import pprint              
WEBFINGER_FILE=".well-known/webfinger"
with open(WEBFINGER_FILE) as f:
    data=f.read()
data=json.loads(data)
pprint(data)
print(json.dumps.__doc__)
with open(WEBFINGER_FILE,"wt") as f:
    f.write(json.dumps(data,indent=4))

