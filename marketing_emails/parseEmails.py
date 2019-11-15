import json
import requests

#APIKey for FROM Portal
ToAPIKey = ""
# APIKey for TO portal
FromAPIKey = ""

offset = 250
get_url = 'https://api.hubapi.com/marketing-emails/v1/emails?limit=250&offset=' + str(offset) + '&hapikey=' + FromAPIKey
post_url = 'https://api.hubapi.com/marketing-emails/v1/emails?hapikey=' + ToAPIKey


def getEmails():
    r = requests.get(url = get_url) 
    data = r.json() 
    return data

def saveRawJSONToFile(data):
    print('from saveRawJSONToFile')
    with open('raw.json', 'w') as json_file:
        json_file.write(json.dumps(data))

def exploreData(data):
    for email in data["objects"]:
        print(email)

def create_POSTable_emails(data):
    print("from create_POSTable_email")
    postable_emails = []
    for email in data['objects']:
        new_email = dict()
        new_email['name'] = email['name']
        new_email['subject'] = email['subject']
        if 'body' in email.keys():
            new_email['body'] = email['body']
        if 'ab' in email.keys():
            new_email['ab'] = email['ab']
        if 'abHoursToWait' in email.keys():
            new_email['abHoursToWait'] = email['abHoursToWait']
        if 'abSampleSizeDefault' in email.keys():
            new_email['abSampleSizeDefault'] = email['abSampleSizeDefault']
        if 'abSuccessMetric' in email.keys():
            new_email['abSuccessMetric'] = email['abSuccessMetric']
        if 'abTestPercentage' in email.keys():
            new_email['abTestPercentage'] = email['abTestPercentage']
        if 'abVariation' in email.keys():
            new_email['abVariation'] = email['abVariation']
        if 'absoluteUrl' in email.keys():
            new_email['absoluteUrl'] = email['absoluteUrl']
        if 'analyticsPageId' in email.keys():
            new_email['analyticsPageId'] = email['analyticsPageId']
        if 'analyticsPageType' in email.keys():
            new_email['analyticsPageType'] = email['analyticsPageType']
        if 'archived' in email.keys():
            new_email['archived'] = email['archived']
        if 'authorAt' in email.keys():
            new_email['authorAt'] = email['authorAt']
        if 'blogRssSettings' in email.keys():
            new_email['blogRssSettings'] = email['blogRssSettings']
        if 'campaign' in email.keys():
            new_email['campaign'] = email['campaign']
        if 'campaignName' in email.keys():
            new_email['campaignName'] = email['campaignName']
        if 'canSpamSettingsId' in email.keys():
            new_email['canSpamSettingsId'] = email['canSpamSettingsId']
        if 'campaignName' in email.keys():
            new_email['campaignName'] = email['campaignName']
        if 'categoryId' in email.keys():
            new_email['categoryId'] = email['categoryId']
        if 'contentAccessRuleIds' in email.keys():
            new_email['contentAccessRuleIds'] = email['contentAccessRuleIds']
        if 'contentTypeCategory' in email.keys():
            new_email['contentTypeCategory'] = email['contentTypeCategory']
        if 'createPage' in email.keys():
            new_email['createPage'] = email['createPage']
        if 'created' in email.keys():
            new_email['created'] = email['created']
        if 'currentState' in email.keys():
            new_email['currentState'] = email['currentState']
        if 'currentlyPublished' in email.keys():
            new_email['currentlyPublished'] = email['currentlyPublished']
        if 'customReplyTo' in email.keys():
            new_email['customReplyTo'] = email['customReplyTo']
        if 'customReplyToEnabled' in email.keys():
            new_email['customReplyToEnabled'] = email['customReplyToEnabled']
        if 'domain' in email.keys():
            new_email['domain'] = email['domain']
        if 'emailBody' in email.keys():
            new_email['emailBody'] = email['emailBody']
        if 'emailNote' in email.keys():
            new_email['emailNote'] = email['emailNote']
        if 'emailTemplateMode' in email.keys():
            new_email['emailTemplateMode'] = email['emailTemplateMode']
        if 'emailType' in email.keys():
            new_email['emailType'] = email['emailType']
        if 'feedbackEmailCategory' in email.keys():
            new_email['feedbackEmailCategory'] = email['feedbackEmailCategory']
        if 'feedbackSurveyId' in email.keys():
            new_email['feedbackSurveyId'] = email['feedbackSurveyId']
        if 'flexAreas' in email.keys():
            new_email['flexAreas'] = email['flexAreas']
        if 'freezeDate' in email.keys():
            new_email['freezeDate'] = email['freezeDate']
        if 'fromName' in email.keys():
            new_email['fromName'] = email['fromName']
        if 'hasContentAccessRules' in email.keys():
            new_email['hasContentAccessRules'] = email['hasContentAccessRules']
        if 'hsEmailBody' in email.keys():
            new_email['hsEmailBody'] = email['hsEmailBody']
        if 'isGraymailSuppressionEnabled' in email.keys():
            new_email['isGraymailSuppressionEnabled'] = email['isGraymailSuppressionEnabled']
        if 'isLocalTimezoneSend' in email.keys():
            new_email['isLocalTimezoneSend'] = email['isLocalTimezoneSend']
        if 'isPublished' in email.keys():
            new_email['isPublished'] = email['isPublished']
        if 'isRecipientFatigueSuppressionEnabled' in email.keys():
            new_email['isRecipientFatigueSuppressionEnabled'] = email['isRecipientFatigueSuppressionEnabled']
        if 'layoutSections' in email.keys():
            new_email['layoutSections'] = email['layoutSections']
        if 'liveDomain' in email.keys():
            new_email['liveDomain'] = email['liveDomain']
        if 'mailingListsExcluded' in email.keys():
            new_email['mailingListsExcluded'] = email['mailingListsExcluded']
        if 'mailingListsIncluded' in email.keys():
            new_email['mailingListsIncluded'] = email['mailingListsIncluded']
        if 'maxRssEntries' in email.keys():
            new_email['maxRssEntries'] = email['maxRssEntries']
        if 'pageRedirected' in email.keys():
            new_email['pageRedirected'] = email['pageRedirected']
        if 'pastMabExperimentIds' in email.keys():
            new_email['pastMabExperimentIds'] = email['pastMabExperimentIds']
        if 'performableGuid' in email.keys():
            new_email['performableGuid'] = email['performableGuid']
        if 'primaryRichTextModuleHtml' in email.keys():
            new_email['primaryRichTextModuleHtml'] = email['primaryRichTextModuleHtml']
        if 'processingStatus' in email.keys():
            new_email['processingStatus'] = email['processingStatus']
        if 'publishDate' in email.keys():
            new_email['publishDate'] = email['publishDate']
        if 'replyTo' in email.keys():
            new_email['replyTo'] = email['replyTo']
        if 'resolvedDomain' in email.keys():
            new_email['resolvedDomain'] = email['resolvedDomain']
        if 'slug' in email.keys():
            new_email['slug'] = email['slug']
        if 'smartEmailFields' in email.keys():
            new_email['smartEmailFields'] = email['smartEmailFields']
        if 'state' in email.keys():
            new_email['state'] = email['state']
        if 'styleSettings' in email.keys():
            new_email['styleSettings'] = email['styleSettings']
        if 'subcategory' in email.keys():
            new_email['subcategory'] = email['subcategory']
        if 'transactional' in email.keys():
            new_email['transactional'] = email['transactional']
        if 'unpublishedAt' in email.keys():
            new_email['unpublishedAt'] = email['unpublishedAt']
        if 'updated' in email.keys():
            new_email['updated'] = email['updated']
        if 'url' in email.keys():
            new_email['url'] = email['url']

        postable_emails.append(new_email)
    return postable_emails

def saveCleanJSONToFile(data):
    with open('clean.md', 'a') as f:
        f.writelines(json.dumps(data) + "\n")
        f.writelines("\n")
        # f.write(json.dumps(data))


def importEmails(data):
    print('from importEmails')
    print(data)
    for email in data:
        body = json.dumps(email)
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        print(body)
        r = requests.post(post_url, data=json.dumps(email), headers=headers)
        print(r.status_code)
        print(r.text)
        print(r.reason)

data_as_dict = getEmails()
print(data_as_dict)
saveRawJSONToFile(data_as_dict)
postable_data = create_POSTable_emails(data_as_dict)
for email in postable_data:
    saveCleanJSONToFile(email)
importEmails(postable_data)
print('limit: ', data_as_dict['limit'])
print('total: ', data_as_dict['total'])
print('total count: ', data_as_dict['totalCount'])
print('Offset: ', data_as_dict['offset'])
