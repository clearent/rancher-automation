import sys
import asyncio
import requests
import websockets
import common
import functools
import signal

rancherUrl = sys.argv[1]
environmentName = sys.argv[2]
serviceName = sys.argv[3]
user = sys.argv[4]
secret = sys.argv[5]

async def listen(url):
    async with websockets.connect(url) as websocket:
        while True:
            log = await websocket.recv()
            print(log)

environment = common.getEnvironment(rancherUrl, environmentName, user, secret)
service = common.getService(rancherUrl, environment["id"], serviceName, user, secret)
containerId = common.getContainerInstance(rancherUrl, environment["id"], service["id"], 0, user, secret)

response = requests.post(rancherUrl+'/v1/projects/'+environment["id"]+'/containers/'+containerId+'/?action=logs', json="{follow:true, lines=100}", auth=(user, secret))
response.raise_for_status()
jsonResponse = response.json()
url = jsonResponse["url"]
token = jsonResponse["token"]

try:
    asyncio.get_event_loop().run_until_complete(listen(url+'/?token='+token))
finally:
    loop.close()
