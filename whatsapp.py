from twilio.rest import Client
from PIL import Image
import os
account_sid = 'ACa367a7fa7626d63b31766e932a413302'
auth_token = '054340de643462c1f267de50d9315ca0'
client = Client(account_sid, auth_token)


# +14155238886
dirpath = os.path.dirname(os.path.realpath(__file__))

img = Image.open(dirpath+'./1.total_outstanding.png')
# img.show()

def send_msg():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Test msg',
        media_url='https://upload.wikimedia.org/wikipedia/commons/5/58/SMirC-silent.svg',
        to='whatsapp:+8801521426578'
    )
    print(message.sid)
