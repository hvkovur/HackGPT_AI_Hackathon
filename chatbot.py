import os
from dotenv import load_dotenv
import google.generativeai as genai
from linkedin_api import Linkedin
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

class ChatBot:
    def __init__(self):
        google_api_key = os.getenv('GOOGLE_API_KEY')
        linkedin_email = os.getenv('LINKEDIN_EMAIL')
        linkedin_password = os.getenv('LINKEDIN_PASSWORD')

        if not all([google_api_key, linkedin_email, linkedin_password]):
            raise ValueError("You are missing a username or password.")

        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

        self.linkedin_api = Linkedin(linkedin_email, linkedin_password)

        self.keyword_to_courses = {
            "data analysis": ["Data Science Specialization", "Google Data Analytics Certificate"],
            "machine learning": ["Artifical Intelligence Fundamentals", "AI Data Analytics and Knowledge Mining","Generative AI", "Machine And Deep Learning", "Responsible AI" ],
            "python": ["Python for Beginners", "Python in Artifical Intelligence"],
            "artificial intelligence": ["Artifical Intelligence Fundamentals", "AI Data Analytics and Knowledge Mining","Generative AI", "Machine And Deep Learning", "Responsible AI" ],
            "cybersecurity": ["Introduction to Cybersecurity", "Cybersecurity Certification Course"],
        }

    def get_linkedin_profile(self, profile_identifier):
        try:
            profile = self.linkedin_api.get_profile(profile_identifier)
            return profile
        except Exception as e:
            print(f"Error retrieving LinkedIn profile: {e}")
            return None

    def suggest_courses(self, profile):
        skills = profile.get("skills", [])
        headline = profile.get("headline", "")
        summary = profile.get("summary", "")

        content_list = []

        if isinstance(skills, list):
            for skill in skills:
                if isinstance(skill, str):
                    content_list.append(skill)
                elif isinstance(skill, dict):
                    content_list.append(skill.get("name", ""))

        if isinstance(headline, str):
            content_list.append(headline)
        if isinstance(summary, str):
            content_list.append(summary)

        matched_courses = set()
        for keyword, courses in self.keyword_to_courses.items():
            if any(keyword in content.lower() for content in content_list if isinstance(content, str)):
                matched_courses.update(courses)

        return list(matched_courses)

    def handle_chat(self, user_input):
        if user_input.startswith('linkedin '):
            profile_id = user_input.split(' ', 1)[1]
            profile = self.get_linkedin_profile(profile_id)
            if profile:
                suggested_courses = self.suggest_courses(profile)
                if suggested_courses:
                    return f"Based on the profile, here are some courses you might find helpful:<br>" + "<br>".join(f"- {course}" for course in suggested_courses)
                else:
                    return "No relevant courses found based on the profile."
            else:
                return "Could not retrieve the LinkedIn profile."

        try:
            response = self.chat.send_message(user_input, stream=True)
            full_response = ""
            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
            return full_response
        except Exception as e:
            return f"Sorry, an error occurred: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    chatbot = ChatBot()
    data = request.get_json()
    user_input = data.get('user_input', '')
    
    response = chatbot.handle_chat(user_input)
    
    return jsonify({"response": response})

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()