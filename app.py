from flask import Flask, render_template, request, jsonify  # type: ignore
from textblob import TextBlob  # type: ignore
import random  # For dynamic responses
import logging  # For debugging

# Initialize Flask
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')  # Serves the index.html file

# Route to handle chatbot responses
@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        # Extract the user input from the POST request
        user_input = request.json.get('message', '')
        
        # Log the user input for debugging
        logging.info(f"User Input: {user_input}")
        
        # Ensure the input is not empty
        if not user_input.strip():
            return jsonify({'response': "Please enter a valid message."})
        
        # Perform sentiment analysis
        analysis = TextBlob(user_input)
        sentiment = analysis.sentiment.polarity
        
        # Log the sentiment score for debugging
        logging.info(f"Sentiment Score: {sentiment}")
        
        # Generate responses based on sentiment
        positive_responses = [
            "I'm glad to hear you're feeling positive! 😊",
            "That's wonderful! Keep smiling! 😄",
            "Positivity suits you! 🌟"
        ]
        neutral_responses = [
            "I'm here to help! How can I assist you today? 🤝",
            "Feel free to share anything on your mind. I'm listening. 👂",
            "I'm here for you. What's on your mind?"
        ]
        negative_responses = [
            "I'm sorry to hear that. Remember to take care of yourself. 🌻",
            "I'm here if you need to talk. Stay strong. 💪",
            "Things will get better. Hang in there. ❤️"
        ]

        if sentiment > 0:
            chatbot_response = random.choice(positive_responses)
        elif sentiment < 0:
            chatbot_response = random.choice(negative_responses)
        else:
            chatbot_response = random.choice(neutral_responses)

        # Log the response for debugging
        logging.info(f"Chatbot Response: {chatbot_response}")
        
        return jsonify({'response': chatbot_response})
    
    except Exception as e:
        # Log any errors that occur
        logging.error(f"Error: {str(e)}")
        return jsonify({'response': f"Oops! Something went wrong: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
