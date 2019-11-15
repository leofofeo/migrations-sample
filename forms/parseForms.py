import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

get_url = 'https://api.hubapi.com/forms/v2/forms?hapikey=' + FromAPIKey
post_url = 'https://api.hubapi.com/forms/v2/forms?hapikey=' + ToAPIKey

def getForms():
    r = requests.get(url = get_url) 
    data = r.json() 
    return data

def saveRawJSONToFile(data):
    print('from saveRawJSONToFile')
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def exploreData(data):
    for hs_form in (data):
        print("Another form:")
        print(hs_form)

def create_POSTable_forms(data):
    print("from create_POSTable_forms")
    postable_forms = []
    for hs_form in data:
        new_form = dict()
        new_form['name'] = hs_form['name']
        new_form['action'] = hs_form['action']
        new_form['cssClass'] = hs_form['cssClass']
        new_form['submitText'] = hs_form['submitText']
        new_form['formFieldGroups'] = hs_form['formFieldGroups']
        new_form['metaData'] = hs_form['metaData']
        new_form['deletable'] = hs_form['deletable']
        postable_forms.append(new_form)
    return postable_forms

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))


def importForms(data):
    print('from importForms')
    print(data)
    for hs_form in data:
        body = json.dumps(hs_form)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(post_url, data=json.dumps(hs_form), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)

data = getForms()
# saveRawJSONToFile(data)
clean_forms = create_POSTable_forms(data)
# exploreData(clean_forms)
importForms(clean_forms)