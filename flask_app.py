from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  
    print(f"Received user input: {user_input}")  

    if user_input.lower().startswith('linkedin '):
        profile_id = user_input.split(' ', 1)[1]
        profile = chatbot.get_linkedin_profile(profile_id)
        print(f"Profile retrieved: {profile}") 

        if profile:
            suggested_courses = chatbot.suggest_courses(profile)
            print(f"Suggested courses: {suggested_courses}") 
            return jsonify({"message": f"Here are some courses you might find helpful: {', '.join(suggested_courses)}"})
        else:
            return jsonify({"message": "Could not retrieve the LinkedIn profile."})
    else:
        # Regular chatbot interaction
        response = chatbot.get_response(user_input)
        print(f"Chatbot response: {response}")  
        return jsonify({"message": response})

if __name__ == "__main__":
    app.run(debug=True)
