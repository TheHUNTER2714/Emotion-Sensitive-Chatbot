from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')  # Serves the index.html file

# Route to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']  # Extract message from POST request
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment.polarity  # Perform sentiment analysis
    
    if sentiment > 0:
        chatbot_response = "I'm glad to hear you're feeling positive! 😊"
    elif sentiment < 0:
        chatbot_response = "I'm sorry to hear that. Remember to take care of yourself. 🌻"
    else:
        chatbot_response = "I'm here to help! How can I assist you today? 🤝"
    
    return jsonify({'response': chatbot_response})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
