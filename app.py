from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({'status': 'ok'})

@app.route('/palindromos/<string:phrase>', methods=['GET'])
def palindromo (phrase: str):
    phrase = phrase.replace('_', '')
    phrase = phrase.lower()
    phrase_low = phrase[::-1]
    if phrase == phrase_low:
      #Sort of every character in the phrase
      res = {i : phrase.count(i) for i in set(phrase)}
      #lenght of the phrase 
      letters = len(phrase) - phrase.count(' ')
      #Directory of all the variables
      return jsonify(name = phrase, palindrome='true' ,sorted = res, length = letters)
    else:
      return jsonify(name = phrase, palindrome='false')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)