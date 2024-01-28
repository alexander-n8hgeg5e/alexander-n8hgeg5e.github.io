#!/usr/bin/env python3
import json
from pprint import pprint              
with open("webfinger") as f:
    data=f.read()
with open(".well-known/webfinger","wt") as f:
    f.write(json.dumps(data))

