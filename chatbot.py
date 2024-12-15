import os
from dotenv import load_dotenv
import google.generativeai as genai
from linkedin_api import Linkedin 

# Load environment variables from a .env file
load_dotenv()

class ChatBot:
    def __init__(self):
        # Loads API keys and login credentials using env variables
        google_api_key = os.getenv('GOOGLE_API_KEY')
        linkedin_email = os.getenv('LINKEDIN_EMAIL')
        linkedin_password = os.getenv('LINKEDIN_PASSWORD')

        if not all([google_api_key, linkedin_email, linkedin_password]):
            raise ValueError("Missing one or more environment variables.")

        # Configures Google Generative AI
        genai.configure(api_key=google_api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])

        self.linkedin_api = Linkedin(linkedin_email, linkedin_password)

    def get_linkedin_profile(self, profile_identifier):
        try:
            profile = self.linkedin_api.get_profile(profile_identifier)
            return profile
        except Exception as e:
            print(f"Error retrieving LinkedIn profile: {e}")
            return None

    def conversation(self):
        print("Chatbot: Hello! How can I help you today? \nType 'exit' to end the conversation.")
        print("You can also type 'linkedin [profile]' to fetch a LinkedIn profile.")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

            if user_input.startswith('linkedin '):
                profile_id = user_input.split(' ', 1)[1]
                profile = self.get_linkedin_profile(profile_id)
                if profile:
                    print("LinkedIn Profile:", profile)
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
