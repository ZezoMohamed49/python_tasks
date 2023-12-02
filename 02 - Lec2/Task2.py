'''
Task2
1 - suggest activities
2 - get location
'''

import requests

################################## To get activities ####################################
response =requests.get(r"https://www.boredapi.com/api/activity")

print("Activities :")
print(response.json())

################################# To get your location ##################################

Ip = requests.get(r"https://api.ipify.org/?format=json")                         # Get Ip

location = requests.get(r'https://ipinfo.io/{}/geo'.format(Ip.json()['ip']))     # Get location
print(location.json())

