import sys
import requests
import common

rancherUrl=sys.argv[1]
environmentName=sys.argv[2]
stackName=sys.argv[3]

environment=common.getEnvironment(rancherUrl, environmentName)
stack = common.getStack(rancherUrl, environment["id"], stackName)

healthState="unknown"
if stack!=None:
        healthState=stack["healthState"]

print "Stack " + stackName + " in " + environmentName + " is " + healthState