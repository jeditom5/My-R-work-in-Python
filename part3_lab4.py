#!/usr/bin/python3

import os, requests, re, glob

def convert_weight(wstr):
    #  The weight string or wstr for short is formatted as '100 lbs'.
    #  So when we split on ' '. The resulting array is ['100', 'lbs'].
    weight_arr = wstr.split(" ")
    #  In this case, we only want integers in the weight field according to the lab.
    #  So we use the 0th element
    weight = int(weight_arr[0])
    return weight
## sample payload looks like the following:
## {
#     "name": "Test Fruit",
#     "weight": 100,
#     "description":"This is the description of my test fruit",
#     "image_name": "icon.sheet.png"
##  }
def generate_payload(filename):
    payload = {}
    pattern =  r"\.txt"
    image_name = re.sub(pattern,".jpeg",filename)
    with open(filename) as f:
        payload["name"] = f.readline().rstrip()
        payload["weight"] =  convert_weight(f.readline().rstrip())
        payload["description"] = f.readline().rstrip()
        payload["image_name"] = image_name
    return payload
def send(payload):
    ## TODO add url
    request = requests.post("http://[external-IP-address]/fruits/",json=payload)
    return request

def main():
    for file in glob.glob(os.getcwd()+'/supplier-data/descriptions/*'):
        payload = generate_payload(file)
        send(payload)

if __name__ == "__main__":
    main()