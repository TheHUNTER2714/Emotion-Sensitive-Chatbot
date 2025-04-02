from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Function to detect emotion and generate response
def detect_emotion_and_respond(message):
    # Basic sentiment analysis using TextBlob
    analysis = TextBlob(message)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0:
        return "I'm glad to hear you're feeling positive! 😊"
    elif sentiment < 0:
        return "I'm sorry to hear that. If you're feeling down, remember to take care of yourself. 🌻"
    else:
        return "I'm here to help! How can I assist you today? 🤝"

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    chatbot_response = detect_emotion_and_respond(user_input)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
