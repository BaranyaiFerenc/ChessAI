
import scanner
import requests
import json

json_data = '{ "fen" : "%s" }'% (scanner.run_scanner('source/chess1.png')+' b - - 1 2')
json_data = json.loads(json_data)


url = 'https://chess-api.com/v1'


print(json_data)

x = requests.post(url, json = json_data)

print(x.text)