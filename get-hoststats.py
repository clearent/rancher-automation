import sys
import requests
import common

rancherUrl = sys.argv[1]
environmentName = sys.argv[2]
user=sys.argv[3]
secret=sys.argv[4]

environment = common.getEnvironment(rancherUrl, environmentName, user, secret)

response = requests.get(rancherUrl+'/v1/projects/'+environment["id"]+'/hosts', auth=(user, secret))
response.raise_for_status()
hosts = response.json()

for host in hosts["data"]:
    print("hostName: " + host["hostname"])
    print(" Memory Info:")
    print("     memTotal: " + str(host["info"]["memoryInfo"]["memTotal"]))
    print("     swapTotal: " + str(host["info"]["memoryInfo"]["swapTotal"]))
    print("     cached: " + str(host["info"]["memoryInfo"]["cached"]))
    print("     swapCached: " + str(host["info"]["memoryInfo"]["swapCached"]))
    print("     swapFree: " + str(host["info"]["memoryInfo"]["swapFree"]))
    print("     memAvailable: " + str(host["info"]["memoryInfo"]["memAvailable"]))
    print("     memFree: " + str(host["info"]["memoryInfo"]["memFree"]))
    print("     inactive: " + str(host["info"]["memoryInfo"]["inactive"]))
    print("     active: " + str(host["info"]["memoryInfo"]["active"]))
    print("     buffers: " + str(host["info"]["memoryInfo"]["buffers"]))
    print(" CPU Info:")
    print("     cpuCorePercentages: " + str(host["info"]["cpuInfo"]["cpuCoresPercentages"]))
    print("     loadAvg: " + str(host["info"]["cpuInfo"]["loadAvg"]))
