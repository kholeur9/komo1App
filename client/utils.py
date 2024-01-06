import vonage
import os

client = vonage.Client(key= os.environ['NEXTMO_API_KEY'],secret= os.environ['NEXTMO_API_SECRET'])
sms = vonage.Sms(client)

def demande_credit(message):
  print('Message à envoyer : ' + message)
  response = sms.send_message({
    'from': "Komo1App",
    'to': "0024177036839",
    'text': message,
  })

  if response["messages"][0]['status'] == '0':
    print(f"Message sent successfully. Message ID: {response['message-id']}")
  else:
    print(f"Echec de l'envoi du message. Erreur: {response['error-text']}")