import requests
import json
import pandas as pd

url = "http://api.open-notify.org/astros.json"

x = requests.get(url).text
x = json.loads(x)
people = x["people"]
table = pd.DataFrame(people)
table_no_index = table.to_string(index=False)
print("People currently in space: ")
print(table_no_index)





