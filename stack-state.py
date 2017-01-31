import sys
import requests
import common

rancherUrl = sys.argv[1]
environmentName = sys.argv[2]
stackName = sys.argv[3]
user = sys.argv[4]
secret = sys.argv[5]

environment = common.getEnvironment(rancherUrl, environmentName, user, secret)
stack = common.getStack(rancherUrl, environment["id"], stackName, user, secret)

healthState = "unknown"
if stack != None:
        healthState=stack["healthState"]

print("Stack " + stackName + " in " + environmentName + " is " + healthState)
