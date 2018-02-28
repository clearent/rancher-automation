# rancher-automation
A set of scripts for interacting with the Rancher API

# common.py

# get-containerlogs.py

# get-hoststats.py

# scale-service.py

# service-state.py

# stack-state.py

# storm-mitigate.py
## Usage
#### Arguments
This file takes one argument, which should be a text file
##### Text File Format
BaseURL
EnvironmentID
Rancher API Access key
Rancher API Secret key
## Function
This script helps to mitigate what is known as a "Boot Storm" when a Rancher environment crashes and all services are fighting for resources when trying to start at the same time
This script also needs your environment to have custom user labels on all services called "Service_Class" and prioritized as follows: A+,A,B,C
This script then shuts down all services, and then starts them back up in order based on their priority
