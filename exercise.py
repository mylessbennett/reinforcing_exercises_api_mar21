import requests


ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')

dict = ottawa_wards_response.json()

for ward in dict['objects']:
    name = ward['name']
    print("Ward Name: {}".format(name))

representatives_response = requests.get('https://represent.opennorth.ca/representatives/house-of-commons/')

dict2 = representatives_response.json()

for representative in dict2['objects']:
    name = representative['name']
    print("Representative Name:{}".format(name))
