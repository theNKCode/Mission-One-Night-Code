from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'nikhilkamblestudy@gmail.com'
email_password = 'vfhu ozbx uwwu bynz'


email_receivers = [
    'nikhilkamble9130@gmail.com',
    '21070317@ycce.in',
    'ctycc23cse601@iiitn.ac.in'
]


subject = "Testing mail through python"
body = """This is a mail sent through Python!"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    for email_receiver in email_receivers:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f'Email sent to {email_receiver}')