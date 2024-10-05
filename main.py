import imaplib
import email
from email.header import decode_header
import time
import env
from modules.ai.main import respondMessage

# Account credentials
username = env.email
password = env.emailPassword

# Connect to the server
mail = imaplib.IMAP4_SSL("imap.gmail.com")

# Login to your account
mail.login(username, password)

# Select the mailbox you want to use
mail.select("inbox")

def process_mailbox(mail):
    status, messages = mail.search(None, "UNSEEN")
    if status == "OK":
        for num in messages[0].split():
            status, msg_data = mail.fetch(num, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    print("New email:", subject.lower())
                    # checkEmailSubject(subject)

                    # Get the sender's email address
                    from_ = msg.get("From")
                    print("From:", from_)
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if "attachment" not in content_disposition:
                                if content_type == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    print("Body:", body)
                    else:
                        body = msg.get_payload(decode=True).decode()
                        print("Body:", body.lower().replace(' ', '').replace('\r', ''))
                    respondMessage(from_, body)
while True:
    mail.NOOP()
    print("Waiting for new emails...")
    time.sleep(30)  # Check every minute
    process_mailbox(mail)
