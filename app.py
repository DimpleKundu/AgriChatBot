from flask import Flask, jsonify, render_template, request
from chat import interact_with_chatbot

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route('/ask', methods=['POST'])
def ask():
    message = str(request.json['messageText'])

    bot_response = interact_with_chatbot(message)
    return jsonify({'status': 'OK', 'answer': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
