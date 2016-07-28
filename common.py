import sys
import requests

def getEnvironment(rancherUrl, environmentName):
    response = requests.get('http://'+rancherUrl+'/v1/projects')
    data = response.json()

    environment_instance=None
    for environment in data["data"]:
        if environment["name"] == environmentName:
            environment_instance=environment
    
    return environment_instance

def getStack(rancherUrl, environmentId, stackName):
    request = 'http://'+rancherUrl+'/v1/projects/'+environmentId+'/environments?name='+stackName+'&limit=1'
    response = requests.get(request)
    data = response.json()
    stack_instance=None
    for stack in data["data"]:
        if stack["name"] == stackName:
            stack_instance=stack
    return stack_instance

def getService(rancherUrl, environmentId, serviceName):
    request = 'http://'+rancherUrl+'/v1/projects/'+environmentId+'/services?name='+serviceName+'&limit=1'
    response = requests.get(request)
    data = response.json()
    service_instance=None
    for service in data["data"]:
        if service["name"] == serviceName:
            service_instance=service
    return service_instance

def updateService(rancherUrl, environmentId, serviceId, updatedService):
    request = 'http://'+rancherUrl+'/v1/projects/'+environmentId+'/services/'+serviceId
    response = requests.put(request, data=updatedService)
    response.raise_for_status()