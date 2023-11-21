from twilio.rest import Client
import os

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
sender_phone_no = os.environ['TWILIO_PHONE_NO']
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="",
    from_=sender_phone_no,
    body="Hello again")

print(message.sid)