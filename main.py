
import scanner
import requests
import json

import controller
#(scanner.run_scanner('source/chess1.png'))

json_data = '{ "fen" : "%s" }'% controller.CopyFEN().strip()
json_data = json.loads(json_data)


url = 'https://chess-api.com/v1'


print(json_data)

x = requests.post(url, json = json_data)

print(x.text)