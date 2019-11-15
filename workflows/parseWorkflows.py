import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

offset = 0
get_url = 'https://api.hubapi.com/automation/v3/workflows/?hapikey=' + FromAPIKey
post_url = 'https://api.hubapi.com/automation/v3/workflows?hapikey=' + ToAPIKey


def getWorkflows():
    r = requests.get(url = get_url) 
    data = r.json() 
    return data

def getWorkflowMetadata(id):
    wf_url = 'https://api.hubapi.com/automation/v3/workflows/' + str(id) + '/?stats=false&hapikey=' + FromAPIKey
    r = requests.get(url = wf_url)
    data = r.json()
    return data

def saveRawJSONToFile(data):
    print('from saveRawJSONToFile')
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def exploreData(data):
    for wf in data["workflows"]:
        print('New wf: \n')
        print(wf)
        print('\n')

def create_POSTable_workflows(data):
    print("from create_POSTable_workflows")
    postable_wfs = []
    for wf in data['workflows']:
        wf_id = wf['id']
        wf_data = getWorkflowMetadata(wf_id)
        new_wf = dict()
        new_wf['name'] = wf_data['name']
        new_wf['enabled'] = False
        new_wf['type'] = wf_data['type']
        if 'actions' in wf_data.keys():
            new_wf['actions'] = wf_data['actions']
        if 'segmentCriteria' in wf_data.keys():
            new_wf['segmentCriteria'] = wf_data['segmentCriteria']
        if 'goalCriteria' in wf_data.keys():
            new_wf['goalCriteria'] = wf_data['goalCriteria']
        if 'eventAnchor' in wf_data.keys():
            new_wf['eventAnchor'] = wf_data['eventAnchor']
        if 'staticDateAnchor' in wf_data.keys():
            new_wf['staticDateAnchor'] = wf_data['staticDateAnchor']
        if 'contactPropertyAnchor' in wf_data.keys():
            new_wf['contactPropertyAnchor'] = wf_data['contactPropertyAnchor']
        if 'nurtureTimeRange' in wf_data.keys():
            new_wf['nurtureTimeRange'] = wf_data['nurtureTimeRange']
        if 'unenrollmentSetting' in wf_data.keys():
            new_wf['unenrollmentSetting'] = wf_data['unenrollmentSetting']
        if 'suppressionSetting' in wf_data.keys():
            new_wf['suppressionSetting'] = wf_data['suppressionSetting']
        if 'onlyExecOnBizDays' in wf_data.keys():
            new_wf['onlyExecOnBizDays'] = wf_data['onlyExecOnBizDays']
        if 'canEnrollFromSalesforce' in wf_data.keys():
            new_wf['canEnrollFromSalesforce'] = wf_data['canEnrollFromSalesforce']
        if 'allowContactToTriggerMultipleTimes' in wf_data.keys():
            new_wf['allowContactToTriggerMultipleTimes'] = wf_data['allowContactToTriggerMultipleTimes']
        if 'listening' in wf_data.keys():
            new_wf['listening'] = wf_data['listening']
        print(new_wf)
        postable_wfs.append(new_wf)
    return postable_wfs

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")


def importWorkflows(data):
    print('from importWorkflows')
    for wf in data:
        body = json.dumps(wf)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(post_url, data=json.dumps(wf), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)

# print(get_url)
data_as_dict = getWorkflows()
saveRawJSONToFile(data_as_dict)
postable_data = create_POSTable_workflows(data_as_dict)
for wf in postable_data:
    saveCleanJSONToFile(wf)
importWorkflows(postable_data)
