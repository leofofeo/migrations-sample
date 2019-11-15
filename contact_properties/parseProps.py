import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

getURL = 'https://api.hubapi.com/properties/v1/contacts/properties?hapikey=' + FromAPIKey
postURL = 'https://api.hubapi.com/properties/v1/contacts/properties?hapikey=' + ToAPIKey

def getProperties():
    r = requests.get(url = getURL) 
    data = r.json() 
    return data

def saveRawJSONToFile(data):
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def removeHubSpotDefaults(data):
    custom_props = []
    for prop in data:
        new_prop = dict()
        new_prop['options'] = []
        if prop['hubspotDefined'] == True:
            continue
        for k, v in prop.items():
            new_prop[k] = v
        custom_props.append(new_prop)
    return custom_props

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))

def removeUnnecessaryParameters(data):
    spruced_data = []
    for prop in data:
        new_prop = dict()
        new_prop["name"] = prop["name"]
        new_prop["label"] = prop["label"]
        new_prop["groupName"] = prop["groupName"]
        new_prop["type"] = prop["type"]
        if  'fieldType' in prop.keys():
            new_prop["fieldType"] = prop["fieldType"]
        if 'description' in prop.keys():
            new_prop['description'] = prop['description']
        if 'formField' in prop.keys():
            new_prop['formField'] = prop['formField']
        if prop['options']:
            new_prop['options'] = prop['options']
        else:
            new_prop['options'] = []
        if 'displayOrder' in prop.keys():
            new_prop['displayOrder'] = prop['displayOrder']
        spruced_data.append(new_prop)
    return spruced_data

def importProperties(data):
    for idx, prop in enumerate(data):
        body = json.dumps(prop)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(postURL, data=json.dumps(prop), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)


data_as_list = getProperties()
saveRawJSONToFile(data_as_list)
migrateable_data = removeHubSpotDefaults(data_as_list)
for prop in migrateable_data:
    saveCleanJSONToFile(prop)
spruced_data = removeUnnecessaryParameters(migrateable_data)
importProperties(spruced_data)