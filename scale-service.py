import sys
import requests
import common

rancherUrl=sys.argv[1]
environmentName=sys.argv[2]
serviceName=sys.argv[3]
scaleSize=sys.argv[4]

environment=common.getEnvironment(rancherUrl, environmentName)
service=common.getService(rancherUrl, environment["id"], serviceName)

service["scale"]=scaleSize

common.updateService(rancherUrl, environment["id"], service["id"], service)