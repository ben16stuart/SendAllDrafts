from __future__ import print_function
import httplib2
import os
import base64
import sys
import oauth2client

from oauth2client import client, tools, file
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from googleapiclient.http import MediaFileUpload

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = <JSON file>
APPLICATION_NAME = 'Gmail API Python Send Email'


def get_credentials():
    # If needed create folder for credential
    home_dir = os.path.expanduser('~') #>> C:\Users\Me
    credential_dir = os.path.join(home_dir, '.credentials') # >>C:\Users\Me\.credentials   (it's a folder)
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)  #create folder if doesnt exist
    credential_path = os.path.join(credential_dir, 'cred dor med mail.json')
    #Store the credential
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()

    if not credentials or credentials.invalid:
        CLIENT_SECRET_FILE = <JSON file>
        APPLICATION_NAME = 'Gmail API Python Send Email'
        SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
        # Create a flow object. (it assists with OAuth 2.0 steps to get user authorization + credentials)
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store)
    return credentials

def main():
    """Shows basic usage of the Gmail API.
    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    drafts = service.users().drafts()
    result = drafts.list(userId="me",maxResults=2000).execute()
    # print(result["drafts"])
    print(len(result["drafts"]))
    for draft in result["drafts"]:
        draft_id = draft["id"]
        print(draft_id)
        try:
            drafts.send(userId='me', body={ 'id': str(draft_id) }).execute(http=http)
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    main()
