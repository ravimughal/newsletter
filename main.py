from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email_utils import create_message, send_message
from csv_utils import get_emails_from_csv

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('path_to_credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=credentials)

    subject = 'Sua Newsletter Semanal'
    body = 'Olá assinantes! Esta é a nossa última newsletter.'

    csv_filename = 'lista_assinantes.csv'
    subscribers = get_emails_from_csv(csv_filename)

    for subscriber in subscribers:
        message = create_message('testedasilvafilho@gmail.com', subscriber, subject, body)
        send_message(service, 'me', message)

if __name__ == '__main__':
    main()
