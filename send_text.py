from twilio.rest import TwilioRestClient

account_sid = "AC7e7196409563149d8e49b5c77991e455" # Your Account SID from www.twilio.com/console
auth_token  = "acf4b7f95804505e75d1f364d8281b6d"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="I'm Ron Burgundy?",
    to="+17072285996",    # Replace with your phone number
    from_="+17075959642") # Replace with your Twilio number

print(message.sid)