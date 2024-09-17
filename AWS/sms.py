
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello, this is a test message from Twilio!",
    from_='+12628465298',
    to='+919309101444'
)

print(f"Message sent with SID: {message.sid}")