from common import getAllUserStackServices, deactivateService, activateService, untilHealthyCount, untilHealthy, serviceNumByClass
import time
import sys

#declaration of Variables
polling_interval = .1
processThreshold = 3000 #polling interval times processThreshold = polling period
#You will reference a text file that has the URL, Environment ID, Rancher User, and Rancher Secret on separate lines based on the environment, this reads those and captures variables

refFile = open(sys.argv[1])
#This sets the individual lines to the variables for the script
ranURL = refFile.readline().replace("\n","")
ranEnvID = refFile.readline().replace("\n","")
ranUser = refFile.readline().replace("\n","")
ranSecret = refFile.readline().replace("\n","")

#Initally pull .json of each user service
userServices = getAllUserStackServices(ranURL, ranEnvID, ranUser, ranSecret)

#This is to initially deactivate all User services in Rancher
for eachService in range(0,len(userServices)):
    ID = userServices[eachService]['id']
    Name = userServices[eachService]['name']
    deactivateService(ranURL, ranEnvID, ID, Name, ranUser, ranSecret)

time.sleep(10)

#Counting each subclass
APlus = serviceNumByClass(ranURL, ranEnvID, ranUser, ranSecret, 'A+')
A = serviceNumByClass(ranURL, ranEnvID, ranUser, ranSecret, 'A')
A = A + APlus
B = serviceNumByClass(ranURL, ranEnvID, ranUser, ranSecret, 'B')
B = B + A
C = serviceNumByClass(ranURL, ranEnvID, ranUser, ranSecret, 'C')
C = C + B

#This is to start up each User service in Rancher by service_class label
untilHealthy(ranURL, ranEnvID, ranUser, ranSecret, 'A+', APlus, polling_interval, processThreshold)
untilHealthyCount(ranURL, ranEnvID, ranUser, ranSecret, 'A', A, polling_interval, processThreshold)
untilHealthyCount(ranURL, ranEnvID, ranUser, ranSecret, 'B', B, polling_interval, processThreshold)
untilHealthyCount(ranURL, ranEnvID, ranUser, ranSecret, 'C', C, polling_interval, processThreshold)

for eachService in range(0,len(userServices)):
    ID = userServices[eachService]['id']
    Name = userServices[eachService]['name']
    activateService(ranURL, ranEnvID, ID, Name, ranUser, ranSecret)
