# flask_app.py
from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML page

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get message from the frontend
    if user_input.lower().startswith('linkedin '):
        profile_id = user_input.split(' ', 1)[1]
        profile = chatbot.get_linkedin_profile(profile_id)
        if profile:
            suggested_courses = chatbot.suggest_courses(profile)
            return jsonify({"message": f"Here are some courses you might find helpful: {', '.join(suggested_courses)}"})
        else:
            return jsonify({"message": "Could not retrieve the LinkedIn profile."})
    else:
        response = chatbot.get_response(user_input)  # Get chatbot response
        return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
