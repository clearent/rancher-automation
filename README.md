# rancher-automation
A set of scripts for interacting with the Rancher API

# common.py

# get-containerlogs.py

# get-hoststats.py

# scale-service.py

# service-state.py

# stack-state.py

# storm-mitigate.py
### Usage
#### Arguments
This file takes one argument, which should be a text file\s\s
For example: **"python ./storm-mitigate.py text.txt"**
##### Text File Format
BaseURL\s\s
EnvironmentID\s\s
Rancher API Access key\s\s
Rancher API Secret key\s\s
### Function
This script helps to mitigate what is known as a "Boot Storm" when a Rancher environment crashes and all services are fighting for resources when trying to start at the same time.
This script also needs your environment to have custom user labels on all services called *"Service_Class"* and prioritized as follows: **(A+,A,B,C)**\s\s
This script then shuts down all services, and then starts them back up in order based on their priority
