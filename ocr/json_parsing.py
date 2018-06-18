import json
import pandas as pd

columns = ['text', 'bounding_box']
df = pd.DataFrame(columns=columns)
d = {}
try:
    with open('/Users/devpriyadave/git/python/ocr/static/ocr_data.json') as data_file:
        decoded = json.load(data_file)

    # Access data
    for x in decoded['regions']:
        for word in x['lines']:
            bounding_box = word['boundingBox']
            text = ''
            for w in word['words']:
                text = text + w['text'] + ' '
            df = df.append([{'text': text, 'bounding_box': bounding_box}], ignore_index=True)
    print(df)
    #Create dict
    for i,k in df.iterrows():
        if i+1 < len(df.index):
            d[k['text']] = df.iloc[df.index[i+1]]['text']

    #Access relevant data
    print("Branch " ,d['Branch No. '])
    print("account", d['Account No. '])
    print("fa", d['FA/PWA NO. '])

except ():
    print("JSON format error")