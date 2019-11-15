import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

offset = 250
get_url = 'https://api.hubapi.com/contacts/v1/lists?count=250&offset=' + str(offset) + '&hapikey=' + FromAPIKey
post_url = 'https://api.hubapi.com/contacts/v1/lists?count=250&hapikey=' + ToAPIKey


def getLists():
    r = requests.get(url = get_url) 
    data = r.json() 
    return data

def saveRawJSONToFile(data):
    print('from saveRawJSONToFile')
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def exploreData(data):
    for _, hs_list in enumerate(data["lists"]):
        print(hs_list)

def create_POSTable_lists(data):
    print("from create_POSTable_lists")
    postable_lists = []
    for hs_list in data['lists']:
        new_lst = dict()
        new_lst['name'] = hs_list['name']
        if 'dynamic' in hs_list.keys():
            new_lst['dynamic'] = hs_list['dynamic']
        if 'filters' in hs_list.keys():
            new_lst['filters'] = hs_list['filters']
        postable_lists.append(new_lst)
    return postable_lists

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))


def importLists(data):
    print('from importLists')
    print(data)
    for lst in data:
        body = json.dumps(lst)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(post_url, data=json.dumps(lst), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)

print(get_url)
data_as_dict = getLists()
print(data_as_dict)
saveRawJSONToFile(data_as_dict)
postable_data = create_POSTable_lists(data_as_dict)
for lst in postable_data:
    saveCleanJSONToFile(lst)
importLists(postable_data)
print('Has more: ', data_as_dict['has-more'])
print('Offset: ', data_as_dict['offset'])
