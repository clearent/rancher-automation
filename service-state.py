import sys
import requests
import common

rancherUrl = sys.argv[1]
environmentName = sys.argv[2]
serviceName = sys.argv[3]
user = sys.argv[4]
secret = sys.argv[5]

environment = common.getEnvironment(rancherUrl, environmentName, user, secret)
service = common.getService(rancherUrl, environment["id"], serviceName, user, secret)

healthState = "unknown"
if service != None:
    healthState = service["healthState"]

print("Service " + serviceName + " in " + environmentName + " is " + healthState)
