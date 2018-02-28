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
This file takes one argument, which should be a text file\n
For example: <span style="color:blue">"python ./storm-mitigate.py text.txt"</span>
##### Text File Format
BaseURL\n
EnvironmentID\n
Rancher API Access key\n
Rancher API Secret key\n
### Function
This script helps to mitigate what is known as a "Boot Storm" when a Rancher environment crashes and all services are fighting for resources when trying to start at the same time
This script also needs your environment to have custom user labels on all services called <span style="color:blue">"Service_Class"</span> and prioritized as follows: A+,A,B,C
This script then shuts down all services, and then starts them back up in order based on their priority
