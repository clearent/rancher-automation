import sys
import requests

def getEnvironment(rancherUrl, environmentName, user, secret):
    response = requests.get(rancherUrl+'/v1/projects', auth=(user, secret))
    data = response.json()

    environment_instance=None
    for environment in data["data"]:
        if environment["name"] == environmentName:
            environment_instance=environment
    
    return environment_instance

def getStack(rancherUrl, environmentId, stackName, user, secret):
    request = rancherUrl+'/v1/projects/'+environmentId+'/environments?name='+stackName+'&limit=1'
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    stack_instance=None
    for stack in data["data"]:
        if stack["name"] == stackName:
            stack_instance=stack
    return stack_instance

def getService(rancherUrl, environmentId, serviceName, user, secret):
    request = rancherUrl+'/v1/projects/'+environmentId+'/services?name='+serviceName+'&limit=1'
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    service_instance=None
    for service in data["data"]:
        if service["name"] == serviceName:
            service_instance=service
    return service_instance

def updateService(rancherUrl, environmentId, serviceId, updatedService, user, secret):
    request = rancherUrl+'/v1/projects/'+environmentId+'/services/'+serviceId
    response = requests.put(request, data=updatedService, auth=(user, secret))
    response.raise_for_status()

def getContainerInstance(rancherUrl, environmentId, serviceId, instanceIndex, user, secret):
    response = requests.get(rancherUrl+'/v1/projects/'+environmentId+'/services/'+serviceId+'/instances', auth=(user, secret))
    response.raise_for_status()
    return response.json()["data"][instanceIndex]["id"]