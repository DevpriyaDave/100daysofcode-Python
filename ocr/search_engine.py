import nltk as nl
from collections import Counter

from flask import Flask
from flask import render_template, request, jsonify, json

app = Flask(__name__)








example = " I want to make check deposit to account 101 201111 "
example2 = "transfer 1000 dollars from 1012898 to 120930293"

index = {
    'transfer': ['ach-out', 'ach-in', 'internal'],
    'move': ['ach-out', 'ach-in', 'internal'],
    'wires': ['incoming wire', 'outgoing wire'],
    'check': ['check deposit', 'foreign check deposit', 'check exceptions'],
    'deposit': ['check deposit', 'deposit inquiry', 'deposit exception', 'foreign check deposit'],
    'ach': ['ach-out', 'ach-in', 'ach inquiry', 'ach exception']
}


# pos
# get the intersection of words
# to and from account number
# person name
# synonym of transfer

# relations
# TO find next CD => possible account
# IN find next CD => possible account
#
def process_query(data):
    print(data)
    tokenize = nl.word_tokenize(data)
    pos = nl.pos_tag(tokenize)
    print(pos)
    response = {}
    s1 = []
    for word in index.keys():
        if word in tokenize:
            s1 = index[word] + s1
    final_list = [k for k, v in Counter(s1).items() if v > 1]
    if not final_list:
        final_list = s1
    response['list'] = final_list
    for i in range(0, len(pos)):
        if pos[i][1] == 'IN':
            for k in range(i, len(pos)):
                if pos[k][1] == 'CD':
                    print('from account', pos[k][0])
                    response['from'] = pos[k][0]
                    break
        if pos[i][1] == 'TO':
            temp = 0
            for k in range(i, len(pos)):
                temp = temp + 1
                if pos[k][1] == 'CD':
                    print('TO account', pos[k][0])
                    response['to'] = pos[k][0]
                    break
                if temp > 3:
                    break

    return json.dumps(response)

# while True:
#     data = input("Please enter search query ")
#
#     if data == 'exit':
#         break
#     else:
#         process_query(data)
#         continue

@app.route('/landingpage')
def landingpage():
    return render_template('index.html')

@app.route('/formprocessing')
def formprocessing():
    return render_template('formprocessing.html')

@app.route('/processtext', methods=['POST'])
def processtext():
    data = request.form['text']

    # a = request.args.get('', 0, type=int)
    # b = request.args.get('b', 0, type=int)
    return process_query(data)

if __name__ == "__main__":
    app.run(debug=True)