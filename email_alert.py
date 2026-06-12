import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email,
               customer_name,
               probability):

    sender_email = "Your Mail@gmail.com"

    app_password = "YOUR_APP_PASSWORD"

    subject = "NPA Early Warning Alert"

    body = f"""
Dear {customer_name},

Our monitoring system has detected that your loan account
shows a high probability of becoming a Non-Performing Asset (NPA).

Risk Probability: {probability:.2f}%

Please contact the bank and clear any overdue dues immediately.

Thank You,
South Indian Bank
"""

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()

        server.login(sender_email, app_password)

        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )

        server.quit()

        return True

    except Exception as e:

        print("Email Error:", e)

        return False