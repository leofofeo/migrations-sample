import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

getURL = 'https://api.hubapi.com/properties/v1/contacts/groups?hapikey=' + FromAPIKey
postURL = 'https://api.hubapi.com/properties/v1/contacts/groups?hapikey=' + ToAPIKey

def getGroupsToCreate():
    newPortal = requests.get(url = postURL) 
    oldPortal = requests.get(url = getURL)
    newPortalData = newPortal.json() 
    oldPortalData = oldPortal.json()
    new_portal_groups = []
    for group in newPortalData:
        new_portal_groups.append(group['name'])
    groups_to_create = []
    for group in oldPortalData:
        if group['name'] not in new_portal_groups:
            groups_to_create.append(group)
    print(groups_to_create)
    return groups_to_create

def saveRawJSONToFile(data):
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def removeHubSpotDefaults(data):
    custom_groups = []
    for group in data:
        new_group = dict()
        new_group['options'] = []
        if group['hubspotDefined'] == True:
            continue
        for k, v in group.items():
            if group[k]:
                new_group[k] = v
        custom_groups.append(new_group)
    return new_group

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))

def importGroups(data):
    for _, group in enumerate(data):
        body = json.dumps(group)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(postURL, data=body, headers=headers)
        print(r)


data_as_list = getGroupsToCreate()
saveRawJSONToFile(data_as_list)
for prop in data_as_list:
    saveCleanJSONToFile(prop)
print(data_as_list)
importGroups(data_as_list)