import os
from dotenv import load_dotenv
import google.generativeai as genai
from linkedin_api import Linkedin

# Load environment variables from a .env file
load_dotenv()

class ChatBot:
    def __init__(self):
        # Load API keys and login credentials
        google_api_key = os.getenv('GOOGLE_API_KEY')
        linkedin_email = os.getenv('LINKEDIN_EMAIL')
        linkedin_password = os.getenv('LINKEDIN_PASSWORD')

        if not all([google_api_key, linkedin_email, linkedin_password]):
            raise ValueError("Missing one or more environment variables.")

        # Configure Google Generative AI
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

        self.linkedin_api = Linkedin(linkedin_email, linkedin_password)

        # Define a hardcoded dictionary to map keywords to courses
        self.keyword_to_courses = {
            "data analysis": ["Data Science Specialization by Coursera", "Google Data Analytics Certificate"],
            "machine learning": ["Machine Learning by Andrew Ng (Coursera)", "Deep Learning Specialization"],
            "project management": ["PMP Certification", "Google Project Management Certificate"],
            "python": ["Python for Everybody Specialization", "Automate the Boring Stuff with Python"],
            "cybersecurity": ["Certified Ethical Hacker (CEH)", "Introduction to Cybersecurity by Cisco"],
        }

    def get_linkedin_profile(self, profile_identifier):
        try:
            profile = self.linkedin_api.get_profile(profile_identifier)
            return profile
        except Exception as e:
            print(f"Error retrieving LinkedIn profile: {e}")
            return None

    def suggest_courses(self, profile):
        # Extract relevant sections from the profile (e.g., skills, headline, summary)
        skills = profile.get("skills", [])
        headline = profile.get("headline", "")
        summary = profile.get("summary", "")

        # Ensure all content is in string format
        content_list = []

        # Handle skills (assuming they could be dictionaries)
        if isinstance(skills, list):
            for skill in skills:
                if isinstance(skill, str):
                    content_list.append(skill)
                elif isinstance(skill, dict):  # If a skill is a dictionary, extract relevant string value
                    content_list.append(skill.get("name", ""))  # Assuming 'name' key contains skill name

        # Add headline and summary
        if isinstance(headline, str):
            content_list.append(headline)
        if isinstance(summary, str):
            content_list.append(summary)

        # Find courses based on keywords
        matched_courses = set()
        for keyword, courses in self.keyword_to_courses.items():
            if any(keyword in content.lower() for content in content_list if isinstance(content, str)):
                matched_courses.update(courses)

        return list(matched_courses)

    def conversation(self):
        print("Chatbot: Hello! How can I help you today? \nType 'exit' to end the conversation.")
        print("You can also type 'linkedin [profile]' to fetch a LinkedIn profile and suggest courses.")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

            if user_input.startswith('linkedin '):
                profile_id = user_input.split(' ', 1)[1]
                profile = self.get_linkedin_profile(profile_id)
                if profile:
                    #print("LinkedIn Profile:", profile)
                    print("Chatbot: Analyzing the profile to suggest courses...")
                    suggested_courses = self.suggest_courses(profile)
                    if suggested_courses:
                        print("Chatbot: Based on the profile, here are some courses you might find helpful:")
                        for course in suggested_courses:
                            print(f"  - {course}")
                    else:
                        print("Chatbot: No relevant courses found based on the profile.")
                else:
                    print("Chatbot: Could not retrieve the LinkedIn profile.")
                continue

            response = self.chat.send_message(user_input, stream=True)
            print("Chatbot:", end=" ")
            for chunk in response:
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print()


def main():
    chatbot = ChatBot()
    chatbot.conversation()

if __name__ == "__main__":
    main()
