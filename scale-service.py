import sys
import requests
import common

rancherUrl = sys.argv[1]
environmentName = sys.argv[2]
serviceName = sys.argv[3]
scaleSize = sys.argv[4]
user = sys.argv[5]
secret = sys.argv[6]

environment = common.getEnvironment(rancherUrl, environmentName, user, secret)
service = common.getService(rancherUrl, environment["id"], serviceName, user, secret)

service["scale"] = scaleSize

common.updateService(rancherUrl, environment["id"], service["id"], service, user, secret)