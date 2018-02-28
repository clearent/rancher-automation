import sys
import requests
import json
import time

def getEnvironment(rancherUrl, environmentName, user, secret):
    response = requests.get(rancherUrl+'/v1/projects', auth=(user, secret))
    data = response.json()
    environment_instance=None
    for environment in data["data"]:
        if environment["name"] == environmentName:
            environment_instance=environment
    return environment_instance

#based on the environment ID that you put through the script, it pulls a the API info for name in list form of all non-system stacks
def pullAllUserStacksName(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/stacks?system_ne=true'
    response = requests.get(request, auth=(user, secret))
    data = response.json()['data']
    length = len(data)
    stackName = []
    for eachStack in list(range(0,length)):
        stackName.append(json.dumps(data[eachStack]['name']))
        stackName = [quotes.replace('"','') for quotes in stackName]
    return stackName

##based on the environment ID that you put through the script, it pulls a the API info for ID in list form of all non-system stacks
def pullAllUserStacksIds(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/stacks?system_ne=true'
    response = requests.get(request, auth=(user, secret))
    data = response.json()['data']
    length = len(data)
    stackIds = []
    for eachStack in list(range(0,length)):
        stackIds.append(json.dumps(data[eachStack]['id']))
        stackIds = [quotes.replace('"','') for quotes in stackIds]
    return stackIds

#based on the environment ID that you put through the script, it pulls all of the service IDs into list of lists that run in the non-system stacks
def getAllUserStackServices(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services?system_ne=true'
    response = requests.get(request, auth=(user, secret)).json()['data']
    return response

def pullAllUserStackServicesName(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/?system_ne=true'
    response = requests.get(request, auth=(user, secret))
    serviceData = response.json()['data']
    numOfServices = len(serviceData)
    userStackServices = []
    for eachService in list(range(0,numOfServices)):
        userStackServices.append(json.dumps(serviceData[eachService]['name']))
        userStackServices = [quotes.replace('"','') for quotes in userStackServices]
    return userStackServices

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
    request = rancherUrl+'/v1/projects/'+environmentId+'/services?name='+serviceName
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

#based on the Service ID that you run through the script, it pulls the service class label of that service out
#thses are set based on http://clawiki01.clearent.lan/ClearentWiki/index.php?title=Clearent_Service_Classification
def pullServiceLabel(rancherUrl,environmentId, serviceId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    parsed_json = json.dumps(data['launchConfig']['labels']['service_class'])
    service_label = parsed_json.replace('"','')
    return service_label

#based on the Service ID that you run through the script, it pulls the name of that service out
def pullServiceName(rancherUrl,environmentId, serviceId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    parsed_json = json.dumps(data['name'])
    service_name = parsed_json.replace('"','')
    return service_name

def getHealthState(rancherUrl,environmentId, serviceId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    parsed_json = json.dumps(data['healthState'])
    service_health = parsed_json.replace('"','')
    return service_health

def getState(rancherUrl,environmentId, serviceId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId
    response = requests.get(request, auth=(user, secret))
    data = response.json()
    parsed_json = json.dumps(data['state'])
    service_state = parsed_json.replace('"','')
    return service_state

#based on the Service ID that you run through the script, it shuts that service down and prints the status code to the terminal
def deactivateService(rancherUrl,environmentId, serviceId, ServiceName, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId+'/?action=deactivate'
    response = requests.post(request, auth=(user, secret))
    if response.status_code == 202:
        print('Shutting down', ServiceName)

#based on the Service ID that you run through the script, it starts that service and prints the status code to the terminal
def activateService(rancherUrl,environmentId, serviceId, ServiceName, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services/'+serviceId+'/?action=activate'
    response = requests.post(request, auth=(user, secret))
    if response.status_code == 202:
        print('Starting up', ServiceName)

def GetHealthyUserServices(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services?system_ne=true&state=active&healthState=healthy'
    response = requests.get(request, auth=(user, secret)).json()['data']
    return response

def getUnhealthyUserServices(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services?healthState_ne=healthy&system_ne=true'
    response = requests.get(request, auth=(user, secret)).json()['data']
    return response

def getNonStartOnceUserServices(rancherUrl, environmentId, user, secret):
    request = rancherUrl+'/v2-beta/projects/'+environmentId+'/services?system_ne=true&healthState_ne=started-once'
    response = requests.get(request, auth=(user, secret)).json()['data']
    return response

def startAllByClassCount(services, RanURL, EnvID, RanUser, RanSecret, serviceClass):
    count = 0
    step = 3
    for eachService in range(0,len(services)):
        if services[eachService]['launchConfig']['labels']['service_class'] == serviceClass and services[eachService]['healthState'] != 'started-once':
            count += 1
            #if we're still just doing the first 3 of this sublcass, go ahead and start them
            if count <= step:
                ID = services[eachService]['id']
                Name = services[eachService]['name']
                activateService(RanURL, EnvID, ID , Name, RanUser, RanSecret)

def startAllByClass(services, RanURL, EnvID, RanUser, RanSecret, serviceClass):
    for eachService in range(0,len(services)):
        if services[eachService]['launchConfig']['labels']['service_class'] == serviceClass and services[eachService]['healthState'] != 'started-once':
            ID = services[eachService]['id']
            Name = services[eachService]['name']
            activateService(RanURL, EnvID, ID , Name, RanUser, RanSecret)

def untilHealthyCount(RanURL, EnvID, RanUser, RanSecret, serviceClass, limiter, polling_interval, totalPolls):
    loopCount=0
    stillLoop = True
    while len(GetHealthyUserServices(RanURL, EnvID, RanUser, RanSecret)) < limiter and stillLoop == True:
        services = getUnhealthyUserServices(RanURL, EnvID, RanUser, RanSecret)
        startAllByClassCount(services, RanURL, EnvID, RanUser, RanSecret, serviceClass)
        loopCount +=1
        time.sleep(polling_interval)
        #if this operation reaches total polling period, then move on to the next subclass
        if loopCount == totalPolls:
            stillLoop = False

def untilHealthy(RanURL, EnvID, RanUser, RanSecret, serviceClass, limiter, polling_interval, totalPolls):
    loopCount=0
    stillLoop = True
    while len(GetHealthyUserServices(RanURL, EnvID, RanUser, RanSecret)) < limiter and stillLoop == True:
        services = getUnhealthyUserServices(RanURL, EnvID, RanUser, RanSecret)
        startAllByClass(services, RanURL, EnvID, RanUser, RanSecret, serviceClass)
        loopCount += 1
        time.sleep(polling_interval)
        #if this operation reaches total polling period, then move on to the next subclass
        if loopCount == totalPolls:
            stillLoop = False

def serviceNumByClass(RanURL, EnvID, RanUser, RanSecret, serviceClass):
    num = 0
    for eachService in range(0,len(getNonStartOnceUserServices(RanURL, EnvID, RanUser, RanSecret))):
        services = getNonStartOnceUserServices(RanURL, EnvID, RanUser, RanSecret)
        if services[eachService]['launchConfig']['labels']['service_class'] == serviceClass:
            num += 1
    return num
