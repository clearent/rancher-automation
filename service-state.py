import sys
import requests
import common

rancherUrl=sys.argv[1]
environmentName=sys.argv[2]
serviceName=sys.argv[3]

environment=common.getEnvironment(rancherUrl, environmentName)
service=common.getService(rancherUrl, environment["id"], serviceName)

healthState="unknown"
if service != None:
    healthState=service["healthState"]

print "Service " + serviceName + " in " + environmentName + " is " + healthState