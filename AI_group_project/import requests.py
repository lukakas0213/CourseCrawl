import requests

TOKEN = '7767421130:AAGTdmCNuClqEi9kYOET6c_RZKOwUnIl-HM'
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
print(response.json())  # Check the chat ID in the output
