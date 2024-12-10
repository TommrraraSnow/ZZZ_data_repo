import pandas as pd
import json

title = "同色击破+支援的积蓄效率"
result_path = f'Miyabi/{title}.json'
df = pd.read_csv('source.csv')

json_data = df.to_json(orient='records')

with open(result_path, 'w', encoding='utf-8') as f:
    f.write(json_data)