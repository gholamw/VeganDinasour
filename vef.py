# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9d2131f7296e8467f91dc3eccb36fbbb'
auth_token = '6f55716b6fcfaa950f1d4c01e5975813'
client = Client(account_sid, auth_token)

verification_check = client.verify \
                           .services('VA82d8be63c720d53e782b0cf080fdfc72') \
                           .verification_checks \
                           .create(to='+966502014844', code='123456')


#service = client.verify.services.create(friendly_name='The Vegan Dinasour')

#print(service.sid)

print(verification_check.status)