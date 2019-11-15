import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

getURL = 'https://api.hubapi.com/crm-pipelines/v1/pipelines/deals?hapikey=' + FromAPIKey
postURL = 'https://api.hubapi.com/crm-pipelines/v1/pipelines/deals?hapikey=' + ToAPIKey

def getPipelines():
    r = requests.get(url = getURL) 
    data = r.json() 
    return data

def saveRawJSONToFile(data):
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))


def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))


def create_POSTable_data(data):
    migrateable_data = []
    for pipeline in data['results']:
        new_pipeline = dict()
        new_pipeline["pipelineId"] = pipeline["pipelineId"]
        new_pipeline["label"] = pipeline["label"]
        new_pipeline["active"] = pipeline["active"]
        new_pipeline["stages"] = pipeline["stages"]
        new_pipeline["displayOrder"] = pipeline["displayOrder"]
        
        migrateable_data.append(new_pipeline)
    return migrateable_data

def importPipelines(data):
    for prop in data:
        body = json.dumps(prop)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(postURL, data=json.dumps(prop), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)


data_as_list = getPipelines()
saveRawJSONToFile(data_as_list)
migrateable_data = create_POSTable_data(data_as_list)
for prop in migrateable_data:
    saveCleanJSONToFile(prop)
importPipelines(migrateable_data)