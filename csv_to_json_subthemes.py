import pandas as pd
import json

title = "耀嘉音影画对自身输出占比的影响"
result_path = f'Astra/{title}.json'
df = pd.read_csv('source.csv')

json_data = df.to_json(orient='records')

with open(result_path, 'w', encoding='utf-8') as f:
    f.write(json_data)