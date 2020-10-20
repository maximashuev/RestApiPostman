from twilio.rest import Client

client = Client("ACcbb9a272aed2141702026e753988853b", "9d8b943148e5ae6a679b46a4243d76ca")

for msg in client.messages.list():
    print(msg.body)