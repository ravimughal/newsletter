from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import base64
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('path_to_credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=credentials)

    subject = 'Sua Newsletter Semanal'
    body = 'Olá assinantes! Esta é a nossa última newsletter.'

    subscribers = ['ravimughal@hotmail.com', 'assinante2@example.com']

    for subscriber in subscribers:
        message = create_message('seu_email@example.com', subscriber, subject, body)
        send_message(service, 'me', message)

def create_message(sender, to, subject, message_text):
    message = f"From: {sender}\nTo: {to}\nSubject: {subject}\n\n{message_text}"
    raw_message = base64.urlsafe_b64encode(message.encode()).decode()
    return {'raw': raw_message}

def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        print('Mensagem enviada:', message['id'])
    except Exception as e:
        print('Ocorreu um erro:', e)

if __name__ == '__main__':
    main()
