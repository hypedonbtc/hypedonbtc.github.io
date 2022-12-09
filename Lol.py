# Import the necessary modules
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Your Twilio phone number
from_number = 'your_twilio_phone_number'

# Read the phone numbers from a text file, one number per line
with open('phone_numbers.txt', 'r') as f:
    phone_numbers = f.read().splitlines()

# Create a Twilio client
client = Client(account_sid, auth_token)

# Loop through the phone numbers and send a text message to each one
for to_number in phone_numbers:
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body='Hello, this is a test message.'
    )
    print(f'Sent message to {to_number}')
