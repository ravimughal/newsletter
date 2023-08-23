import base64

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
