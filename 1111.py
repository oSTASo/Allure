import json
import requests


response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json').text

answer = json.loads(response)

print(response)
print(answer['insult'])

