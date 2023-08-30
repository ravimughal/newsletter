import tkinter as tk
from tkinter import messagebox
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email_utils import create_message, send_message
from csv_utils import get_emails_from_csv

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class EmailApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Envio de E-mail")

        self.subject_label = tk.Label(root, text="Assunto:")
        self.subject_label.pack()

        self.subject_entry = tk.Entry(root)
        self.subject_entry.pack()

        self.body_label = tk.Label(root, text="Corpo da Mensagem:")
        self.body_label.pack()

        self.body_text = tk.Text(root, height=10, width=40)
        self.body_text.pack()

        self.send_button = tk.Button(root, text="Enviar E-mail", command=self.send_email)
        self.send_button.pack()

    def send_email(self):
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END).strip()

        if subject and body:
            try:
                flow = InstalledAppFlow.from_client_secrets_file('./path_to_credentials.json', SCOPES)
                credentials = flow.run_local_server(port=0)

                service = build('gmail', 'v1', credentials=credentials)

                csv_filename = 'lista_assinantes.csv'
                subscribers = get_emails_from_csv(csv_filename)

                for subscriber in subscribers:
                    try:
                        sender_email = 'testedasilvafilho@gmail.com'  # Remetente padrão
                        message = create_message(sender_email, subscriber, subject, body)
                        send_message(service, 'me', message)
                    except ValueError as e:
                        print(e)

                messagebox.showinfo("Sucesso", "E-mails enviados com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        else:
            messagebox.showerror("Erro", "Preencha o assunto e o corpo da mensagem.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmailApp(root)
    root.mainloop()
