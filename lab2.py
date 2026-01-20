#! /usr/bin/env python3
import os, requests
def handler():
    list_of_files = os.listdir('/data/feedback')
    currentdir = '/data/feedback/'
    for f in list_of_files:
        payload = fileProcessor(currentdir+f)
        response = requests.post('http://<corpweb-external-IP>/feedback/',json=payload)
        print(response.status_code)
        print(response.text)
def fileProcessor(file):
    payload = {}
    with open(file) as f:
        payload['title'] = f.readline().rstrip()
        payload['name'] = f.readline().rstrip()
        payload['date'] = f.readline().rstrip()
        payload['feedback'] = f.readline().rstrip()
    return payload
def main():
    handler()
if __name__ == "__main__":
    main()